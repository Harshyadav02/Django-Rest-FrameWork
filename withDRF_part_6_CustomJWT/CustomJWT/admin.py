from django.contrib import admin
from .models import AJIO
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','ProductName' , 'Price' , 'MRP' , 'Discount', 'URL',]
admin.site.register(AJIO ,EmployeeAdmin )