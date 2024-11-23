from django.db import models


class SveltePage(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Название маршрута
    template = models.FileField(upload_to='svelte_templates/')  # Файл Svelte-шаблона
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
