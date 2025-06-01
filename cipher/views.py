"""
Views for the cipher application.
"""
import datetime
import logging
import hashlib
from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from django.shortcuts import render
from cipher.client import Client
from have_i_been_pwned.settings import server_host, server_port, buf_size, MEDIA_ROOT
from main.forms import CipherForm
from main.models import CipherResults

logger = logging.getLogger('custom_django')

def send_message_to_server(data: str, key: str, action: str) -> str:
    try:
        client = Client(host=server_host, port=server_port, buf_size=buf_size)
        client.generate_keys()
        client.connect()
        client.send_message(f'{action} {data} {key}')
        result = client.get_message()
        client.close()
    except (ValueError, IndexError, EOFError, ConnectionRefusedError):
        result = ''
    return result

def save_result(result: str, request: WSGIRequest):
    now = datetime.datetime.now()
    file_name = f'{request.user.username}{now}'
    file_name = hashlib.sha256(file_name.encode()).hexdigest()
    file_path = f'{MEDIA_ROOT}/{file_name}.txt'
    with open(file_path, 'w') as file:
        file.write(result)
    result_object = CipherResults(file=file_path)
    result_object.save()

def get_result_from_cipher_server(data: str, key: str, action: str) -> str:
    result = ''
    counter = 1
    while (result == '' or result == '\0') and counter <= 10:
        counter += 1
        result = send_message_to_server(data, key, action)
    return result if result else 'Server is not available, try later.'

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
        save_result(result, request)
        context['result'] = result
    else:
        logger.warning('User %s send wrong data to cipher page', request.user.username)
        context['form'] = form
    return render(request, 'cipher/result.html', context)
