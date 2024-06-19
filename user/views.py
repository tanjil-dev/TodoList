from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib import messages

@login_required(login_url='login')
def home(request):
    template = 'list.html'
    return render(request, template_name=template)


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        template = 'login.html'
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect")

        return render(request, template_name=template)


def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        template = 'registration.html'
        form = RegistrationForm()
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data['username']
                messages.success(request, 'Account registered for '+ user)
                return redirect('home')
        context = {
            'form': form
        }
        return render(request, template_name=template, context=context)


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
