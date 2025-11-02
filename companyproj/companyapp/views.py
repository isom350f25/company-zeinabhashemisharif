from django.shortcuts import render
from .models import Employee


def list_employee(request):
  employee = Employee.objects.all().order_by("name") 
  context = {
    'list_employee': employee, 
  }
  return render(request, "employee_list.html", context)
# Create your views here.
