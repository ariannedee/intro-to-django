from django.contrib import admin
from .models import Visits


@admin.register(Visits)
class VisitsAdmin(admin.ModelAdmin):
    pass
