"""Административный интерфейс для управления задачами."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Административный класс для модели Task."""

    list_display = ("title", "description", "completed")


admin.site.register(Task, TaskAdmin)
