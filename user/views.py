from django.shortcuts import render
from todoApi.models import Todo 

def home(request):
    template = 'home.html'
    # todoList = Todo.objects.all()
    context = {
        
    }
    return render(request, context=context, template_name=template)