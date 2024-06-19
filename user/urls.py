from django.urls import path
import user.views as view

urlpatterns = [
    path('', view.home, name='home'),
    path('login/', view.login, name='login'),
    path('registration/', view.registration, name='registration'),
    path('logout/', view.logout, name='logout'),
]