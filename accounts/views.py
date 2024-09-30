from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
# Create your views here.
from django.contrib import messages
from accounts.models import User,OTP
from random import randint
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"خروج با موفقیت انحام شد ")
        return redirect("/")
    messages.error(request,"عملیات ناموفق !")
    return redirect("/")



def login_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        user = authenticate(username=phone,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"ورود با موفقیت انجام شد !")
            return redirect("/")
        else:
            messages.error(request,"کاربر با مشخصات شما یافت نشد !")
            return redirect("/")

    else:
        messages.error(request,"عملیات ناموفق!")
        return redirect("/")








