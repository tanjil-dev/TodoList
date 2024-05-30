from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from todoApi import api_views

urlpatterns = [
    path('apiV1/todo/', include('todoApi.urls')),
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]