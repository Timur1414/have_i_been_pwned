from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
import logging

def logout_view(request):
    logging.info(f'{request.user.username} logged out')
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


class ProfilePage(DetailView, LoginRequiredMixin):
    """
    A view that renders the profile page.
    """
    template_name = 'profile/index.html'
    context_object_name = 'user'

    def get_object(self, queryset = ...):
        """
        Returns the user object for the profile page.
        """
        user = User.objects.get(id=self.kwargs['id'])
        return user

    def get_context_data(self, **kwargs):
        """
        Adds context data to the template.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'
        logging.info(f'User {self.request.user.username} viewed profile of {self.object.username}')
        return context
