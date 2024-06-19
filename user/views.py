from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm

@login_required
def home(request):
    if not request.user.is_authenticated:
        redirect('login')
    template = 'list.html'
    return render(request, template_name=template)


def login(request):
    template = 'login.html'
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form.save()
        redirect('home')
    context = {
        'form': form
    }
    return render(request, template_name=template)


def registration(request):
    template = 'registration.html'
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        form.save()
        redirect('home')
    context = {
        'form': form
    }
    return render(request, template_name=template, context=context)


def logout(request):
    logout(request)
    redirect('login')
