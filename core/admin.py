from django.contrib import admin
from .models import Employee, Department
from . import models

from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin


class EmployeeResource(resources.ModelResource):
    employee = Field()

    class Meta:
        model = Employee
        fields = ('emp_no', 'first_name', 'last_name', 'hire_date', 'birth_date', 'gender', 'created','updated')
        export_order = ('emp_no', 'first_name', 'last_name', 'hire_date', 'birth_date', 'gender','created','updated')


class DepartmentResource(resources.ModelResource):
    department = Field()

    class Meta:
        model = Department
        fields = ('name', 'description', 'created','updated')
        export_order = ('name', 'description', 'created','updated')


@admin.register(models.Employee)
class EmployeeAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = EmployeeResource
    list_display = ('emp_no', 'first_name', 'last_name', 'hire_date' , 'image_tag', 'created', 'updated')
    ordering = ['emp_no']
    search_fields = ['emp_no']


@admin.register(models.Department)
class EmployeeAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = DepartmentResource
    list_display = ('name', 'description', 'created','updated')
    ordering = ['name']
    search_fields = ['name']

