from django.contrib import admin
from .models import Sale
# Register your models here.
@admin.register(Sale)
class SaleRegister(admin.ModelAdmin):
    list_display = ("user","product","tedad","price_kol")
    list_filter = ("user",)