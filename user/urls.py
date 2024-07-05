from django.urls import path
from user.views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logoutUser, name='logout'),
]