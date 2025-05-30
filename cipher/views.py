"""
Views for the cipher application.
"""
import logging
from django.http import Http404
from django.shortcuts import render

from cipher.client import Client
from main.forms import CipherForm

logger = logging.getLogger('custom_django')

def send_message_to_server(data: str, action: str) -> str:
    # server_host = os.environ.get('CIPHER_SERVER_HOST', 'Define me!')
    # server_port = int(os.environ.get('CIPHER_SERVER_PORT', 'Define me!'))
    server_host = '127.0.0.1'
    server_port = 8888
    buf_size = 1024
    client = Client(host=server_host, port=server_port, buf_size=buf_size)
    client.connect()
    client.generate_keys()
    client.send_message('100')
    # client.send_message('100')
    result = client.get_message()
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
    form = CipherForm(request.POST)
    if form.is_valid():
        action = form.cleaned_data['action']
        data = form.cleaned_data['data']
        context['action'] = action
        result = send_message_to_server(data, action)
        context['result'] = result
    else:
        logger.warning('User %s send wrong data to cipher page', request.user.username)
        context['form'] = form
    return render(request, 'cipher/result.html', context)
