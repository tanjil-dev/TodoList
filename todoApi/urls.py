from django.urls import path
from . import api_views as view

urlpatterns = [
    path('list/', view.todoList, name='list'),
    path('add/', view.todoAdd, name='add'),
    path('<int:pk>/', view.todoSingleDetails, name='details'),
    path('edit/<int:pk>/', view.todoEdit, name='edit'),
    path('remove/<int:pk>/', view.todoDelete, name='remove'),
]