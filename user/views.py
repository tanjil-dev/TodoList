from django.shortcuts import render
from todoApi.models import Todo 

def home(request):
    template = 'list.html'
    # todoList = Todo.objects.all()
    context = {
        # 'data': todoList
    }
    return render(request, context=context, template_name=template)