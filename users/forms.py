#from typing import Any
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as ar

attrs = {'class' : 'form-control'}

class UserLoginForm(AuthenticationForm):
    
    

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label=ar('UserName'), widget=forms.TextInput(attrs=attrs))

    password = forms.CharField(label=ar('Password'), widget=forms.PasswordInput(attrs=attrs))

class UserRegisterForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

    firstname = forms.CharField(label=ar('First Name'), widget=forms.TextInput(attrs=attrs))

    lastname = forms.CharField(label=ar('Last Name'), widget=forms.TextInput(attrs=attrs))

    email = forms.CharField(label=ar('Email'), widget=forms.TextInput(attrs=attrs))

    username = forms.CharField(label=ar('UserName'), widget=forms.TextInput(attrs=attrs))

    password1 = forms.CharField(label=ar('Password'),strip=False, widget=forms.PasswordInput(attrs=attrs))

    password2 = forms.CharField(label=ar('Password Conformation'),strip=False, widget=forms.PasswordInput(attrs=attrs))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( 'username', 'email')
