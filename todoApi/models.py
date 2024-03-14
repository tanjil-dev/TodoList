from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=30)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    user_name = models.OneToOneField(User, on_delete=models.DO_NOTHING)