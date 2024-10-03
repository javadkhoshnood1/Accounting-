from django.contrib import admin

# Register your models here.
from .models import Contact

@admin.register(Contact)
class CotactRegister(admin.ModelAdmin):
    list_display = ("user","status","discription")
    