from django.urls import path
from .views import (
    HomeView,
    EmployeeListView,
    EmployeeDetailView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,

    DepartmentListView,
)
from .views import department_create

app_name = "core"

urlpatterns = [
    #path('', views.index, name='index'),
    path('', HomeView.as_view(), name='home'),
    path('employee', EmployeeListView.as_view(), name='employee'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee-add'),
    path('employee/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name="employee-detail"),

    path('department', DepartmentListView.as_view(), name='department-list'),
    path('department/create/', department_create, name='department-create'),

]
