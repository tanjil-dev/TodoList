from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    template = 'list.html'
    return render(request, template_name=template)


def login(request):
    template = 'login.html'
    return render(request, template_name=template)


def registration(request):
    template = 'registration.html'
    return render(request, template_name=template)


def logout(request):
    login(request)
    redirect('login')

def spinthewheel(request):
    template = 'spinTheWheel.html'
    return render(request, template_name=template)
