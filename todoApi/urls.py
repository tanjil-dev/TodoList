from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.todoList, name='list'),
    path('add/', api_views.todoAdd, name='add'),
    path('<int:pk>/', api_views.todoSingleDetails, name='details'),
    path('edit/<int:pk>/', api_views.todoEdit, name='edit'),
    path('remove/<int:pk>/', api_views.todoDelete),
]