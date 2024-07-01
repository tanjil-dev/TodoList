from django.urls import path
from todoApi.api_views import *

urlpatterns = [
    path('list/', todoList, name='list'),
    path('add/', todoAdd, name='add'),
    path('<int:pk>/', todoSingleDetails, name='details'),
    path('edit/<int:pk>/', todoEdit, name='edit'),
    path('remove/<int:pk>/', todoDelete, name='remove'),
]