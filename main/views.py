"""
Views for the main application.
"""
import logging
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, FormView, CreateView
from rest_framework.reverse import reverse_lazy

from main.forms import CipherForm, EmailCreateForm, PasswordCreateForm, PhoneCreateForm, AccountCreateForm
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


class EmailCreatePage(LoginRequiredMixin, CreateView):
    """
    A view that renders the email creation page.
    """
    template_name = 'data/creation/email.html'
    model = EmailData
    form_class = EmailCreateForm
    success_url = reverse_lazy('profile')

    def get_initial(self):
        """
        Sets the initial data for the form.
        """
        initial = super().get_initial()
        initial['user'] = self.request.user
        initial['pwned'] = False
        return initial

    def form_valid(self, form):
        """
        Handles the form submission.
        """
        if form.instance.user != self.request.user:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Adds context data to the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Email'
        return context

class PasswordCreatePage(LoginRequiredMixin, CreateView):
    """
    A view that renders the password creation page.
    """
    template_name = 'data/creation/password.html'
    model = PasswordData
    form_class = PasswordCreateForm
    success_url = reverse_lazy('profile')

    def get_initial(self):
        """
        Sets the initial data for the form.
        """
        initial = super().get_initial()
        initial['user'] = self.request.user
        initial['pwned'] = False
        return initial

    def form_valid(self, form):
        """
        Handles the form submission.
        """
        if form.instance.user != self.request.user:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Adds context data to the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Password'
        return context

class PhoneCreatePage(LoginRequiredMixin, CreateView):
    """
    A view that renders the phone number creation page.
    """
    template_name = 'data/creation/phone.html'
    model = PhoneData
    form_class = PhoneCreateForm
    success_url = reverse_lazy('profile')

    def get_initial(self):
        """
        Sets the initial data for the form.
        """
        initial = super().get_initial()
        initial['user'] = self.request.user
        initial['pwned'] = False
        return initial

    def form_valid(self, form):
        """
        Handles the form submission.
        """
        if form.instance.user != self.request.user:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Adds context data to the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Phone Number'
        return context

class AccountCreatePage(LoginRequiredMixin, CreateView):
    """
    A view that renders the account creation page.
    """
    template_name = 'data/creation/account.html'
    model = Account
    form_class = AccountCreateForm
    success_url = reverse_lazy('profile')

    def get_initial(self):
        """
        Sets the initial data for the form.
        """
        initial = super().get_initial()
        initial['user'] = self.request.user
        initial['pwned'] = False
        return initial

    def form_valid(self, form):
        """
        Handles the form submission.
        """
        if form.instance.user != self.request.user:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Adds context data to the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Account'
        return context
