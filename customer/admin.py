from django.contrib import admin
from .models import Customer
# Register your models here.
@admin.register(Customer)
class CustomerRegister(admin.ModelAdmin):
    list_display = ("phone","user", "fullname", "is_active",'price')