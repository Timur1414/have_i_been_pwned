"""
This file contains the forms for the main application.
"""
from django import forms

from cipher.validators import validate_file_extension
from main.models import EmailData, PhoneData, PasswordData, Account


class EmailCreateForm(forms.ModelForm):
    """
    A form for creating an email.
    """
    class Meta:
        model = EmailData
        fields = ['email', 'user', 'pwned']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(),
            'pwned': forms.HiddenInput(),
        }
        labels = {
            'email': 'Email',
        }

class PasswordCreateForm(forms.ModelForm):
    """
    A form for creating a password.
    """
    class Meta:
        model = PasswordData
        fields = ['password', 'user', 'pwned']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(),
            'pwned': forms.HiddenInput(),
        }
        labels = {
            'password': 'Password',
        }

class PhoneCreateForm(forms.ModelForm):
    """
    A form for creating a phone number.
    """
    class Meta:
        model = PhoneData
        fields = ['phone', 'user', 'pwned']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(),
            'pwned': forms.HiddenInput(),
        }
        labels = {
            'phone': 'Phone Number',
        }

class AccountCreateForm(forms.ModelForm):
    """
    A form for creating an account.
    """
    class Meta:
        model = Account
        fields = ['url', 'login', 'password', 'pwned', 'user']
        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(),
            'pwned': forms.HiddenInput(),
        }
        labels = {
            'url': 'URL to site',
            'login': 'Login',
            'password': 'Password',
        }

class CipherForm(forms.Form):
    """
    A form for a cipher page.
    """
    CHOICES = [
        ('encode', 'Encode'),
        ('decode', 'Decode'),
    ]
    data = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='Text', validators=[validate_file_extension])
    key = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Key')
    action = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), label='Action')
