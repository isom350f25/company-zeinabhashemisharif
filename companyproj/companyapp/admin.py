from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin (admin.ModelAdmin):
    list_display=('name','position','date_of_birth','joined_on','phone_number',)
    list_filter =("joined_on",)
    search_fields=['name','position',]
# Register your models here.
