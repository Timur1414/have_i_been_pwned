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

def send_message_to_server(data: str, action: str) -> str | None:
    try:
        client = Client(host=server_host, port=server_port, buf_size=buf_size)
        client.connect()
        client.generate_keys()
        client.send_message(f'{action} {data}')
        result = client.get_message()
        client.close()
        return result
    except ValueError:
        return ''


def cipher(request):
    if request.method == 'GET':
        logger.warning('User %s GET request to cipher page', request.user.username)
        raise Http404()
    logger.info('User %s POST request to cipher page', request.user.username)
    context = {
        'title': 'Cipher Result',
    }
    form = CipherForm(request.POST)
    if form.is_valid():
        action = form.cleaned_data['action']
        data = form.cleaned_data['data']
        context['action'] = action
        result = ''
        while result == '':
            result = send_message_to_server(data, action)
        context['result'] = result
    else:
        logger.warning('User %s send wrong data to cipher page', request.user.username)
        context['form'] = form
    return render(request, 'cipher/result.html', context)
