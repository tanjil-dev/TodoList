from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.todoList, name='list'),
    # path('todo-add/', views.todoList)
]