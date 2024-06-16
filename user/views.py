from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    template = 'list.html'
    return render(request, template_name=template)