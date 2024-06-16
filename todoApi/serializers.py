from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Todo
from rest_framework.fields import CurrentUserDefault


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'