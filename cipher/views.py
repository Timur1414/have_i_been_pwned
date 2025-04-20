"""
Views for the cipher application.
"""
import logging
from django.http import Http404
from django.shortcuts import render
from main.forms import CipherForm

logger = logging.getLogger('custom_django')

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
        if action == 'encrypt':
            pass
        else:
            pass
        result = 'result'
        context['result'] = result
    else:
        logger.warning('User %s send wrong data to cipher page', request.user.username)
        context['form'] = form
    return render(request, 'cipher/result.html', context)
