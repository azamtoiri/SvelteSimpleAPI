from django.contrib import admin

from .models import SveltePage


@admin.register(SveltePage)
class SveltePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fields = ('name', 'template', 'created_at', 'updated_at')
    ordering = ('name',)
