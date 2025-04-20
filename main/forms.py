"""
This file contains the forms for the main application.
"""
from django import forms

class CipherForm(forms.Form):
    """
    A form for a cipher page.
    """
    CHOICES = [
        ('encode', 'Encode'),
        ('decode', 'Decode'),
    ]
    data = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Data')
    key = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Key')
    action = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), label='Action')
