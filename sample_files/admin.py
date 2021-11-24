from django.contrib import admin

# Register your models here.
from .models import Visits


@admin.register(Visits)
class VisitsAdmin(admin.ModelAdmin):
    pass
