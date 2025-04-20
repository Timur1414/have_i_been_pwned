"""
Views for the main application.
"""
import logging
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, FormView

from main.forms import CipherForm
from main.models import EmailData, PhoneData, Account, PasswordData

logger = logging.getLogger('custom_django')


def logout_view(request):
    logger.info('%s logged out', request.user.username)
    logout(request)
    return redirect('index')


class IndexPage(TemplateView):
    """
    A view that renders the index page.
    """
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        """
        Adds context data to the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Index'
        return context


class ProfilePage(LoginRequiredMixin, DetailView):
    """
    A view that renders the profile page.
    """
    template_name = 'profile/index.html'
    context_object_name = 'user'

    def get_object(self, queryset = ...):
        """
        Returns the user object for the profile page.
        """
        user = self.request.user
        return user

    def get_context_data(self, **kwargs):
        """
        Adds context data to the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'
        logger.info('User %s viewed profile', self.object.username)
        context['passwords'] = PasswordData.get_passwords_by_user(self.object)
        context['emails'] = EmailData.get_emails_by_user(self.object)
        context['phones'] = PhoneData.get_phones_by_user(self.object)
        context['accounts'] = Account.get_accounts_by_user(self.object)
        return context


class CipherPage(LoginRequiredMixin, FormView):
    """
    A view that renders the cipher page.
    """
    template_name = 'cipher/index.html'
    form_class = CipherForm

    def get_context_data(self, **kwargs):
        """
        Adds context data to the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cipher'
        logger.info('User %s viewed cipher page', self.request.user.username)
        return context
