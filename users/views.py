from django.shortcuts import render, redirect
from django.views.generic import CreateView
from users.forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate

class RegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def logout_user(request):
    logout(request)
    return redirect('login')
