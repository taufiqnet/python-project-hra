from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Employee
from itertools import chain
import random
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# def index(request):
#     return render(request, 'index.html')
def error_404_view(request, exception):
    return render(request, '404.html')


class HomeView(ListView):
    paginate_by = 1
    template_name = "index.html"
    queryset = Employee.objects.all()
    context_object_name = "employees"


class EmployeeListView(ListView):
    paginate_by = 10
    template_name = "employee_list.html"
    queryset = Employee.objects.all()
    context_object_name = "employees"


class EmployeeDetailView(DetailView):
    template_name = "employee_detail.html"
    queryset = Employee.objects.all()
    context_object_name = "employee"


class EmployeeCreateView(CreateView):
    template_name = "employee_create.html"
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('core:employee')


class EmployeeUpdateView(UpdateView):
    template_name = "employee_update.html"
    queryset = Employee.objects.all()
    fields = '__all__'
    success_url = reverse_lazy('core:employee')


class EmployeeDeleteView(DeleteView):
    template_name = "employee_delete.html"
    model = Employee
    success_url = reverse_lazy('core:employee')
