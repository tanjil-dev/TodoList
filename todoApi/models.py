from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=30)
    is_done = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Spin(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.name