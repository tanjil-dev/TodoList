from django.urls import path
import user.views as view

urlpatterns = [
    path('', view.home, name='home'),
]