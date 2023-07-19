from django.contrib import admin
from .models import Visit


@admin.register(Visit)
class VisitsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'page', 'username', 'timestamp']
    list_filter = ['page', 'username', 'timestamp']
    search_fields = ['page', 'username']
    readonly_fields = ['timestamp']
