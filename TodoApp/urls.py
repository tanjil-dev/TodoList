from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from todoApi import api_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)

urlpatterns = [
    path('apiV1/todo/', include('todoApi.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
