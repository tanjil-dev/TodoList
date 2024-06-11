from django.contrib import admin
from .models import Todo

admin.site.register(Todo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_done', 'created_at', 'user_name']