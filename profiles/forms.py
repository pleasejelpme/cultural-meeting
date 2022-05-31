from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class RegisterForm(UserCreationForm):
    username    = forms.CharField(max_length=20, help_text='', )
    email       = forms.EmailField(max_length=200, help_text='')
    password1   = forms.CharField(max_length=50, help_text='')
    password2   = forms.CharField(max_length=50, help_text='')

    class Meta:
        model = Perfil
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
