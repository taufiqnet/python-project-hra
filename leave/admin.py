from django.contrib import admin
from . import models


@admin.register(models.Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date','leave_type','reason')
    ordering = ['leave_type']
    search_fields = ['leave_type']