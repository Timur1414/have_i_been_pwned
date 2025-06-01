"""
Views for the cipher application.
"""
import logging
from django.http import Http404
from django.shortcuts import render
from cipher.client import Client
from have_i_been_pwned.settings import server_host, server_port, buf_size
from main.forms import CipherForm

logger = logging.getLogger('custom_django')

def send_message_to_server(data: str, key: str, action: str, client: Client) -> str:
    try:
        client.send_message(f'{action} {key} {data}')
        result = client.get_message()
        return result
    except (ValueError, IndexError, EOFError):
        return ''
    except ConnectionRefusedError:
        return 'Server is not responding'

def get_result_from_cipher_server(data: str, key: str, action: str) -> str:
    client = Client(host=server_host, port=server_port, buf_size=buf_size)
    client.generate_keys()
    client.connect()
    result = ''
    counter = 0
    while result == '':
        result = send_message_to_server(data, key, action, client)
        counter += 1
        if counter > 10:
            client.close()
            return 'Server is not responding'
    client.close()
    return result

def cipher(request):
    if request.method == 'GET':
        logger.warning('User %s GET request to cipher page', request.user.username)
        raise Http404()
    logger.info('User %s POST request to cipher page', request.user.username)
    context = {
        'title': 'Cipher Result',
    }
    form = CipherForm(request.POST, request.FILES)
    if form.is_valid():
        action = form.cleaned_data['action']
        data = form.cleaned_data['data'].read()
        key = form.cleaned_data['key']
        context['action'] = action
        result = get_result_from_cipher_server(data.decode(), key, action)
        context['result'] = result
    else:
        logger.warning('User %s send wrong data to cipher page', request.user.username)
        context['form'] = form
    return render(request, 'cipher/result.html', context)
