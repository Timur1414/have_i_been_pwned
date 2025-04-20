from django import forms

class CipherForm(forms.Form):
    CHOICES = [
        ('encode', 'Encode'),
        ('decode', 'Decode'),
    ]
    data = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    key = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    action = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
