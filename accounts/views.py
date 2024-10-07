from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
# Create your views here.
from django.contrib import messages
import json
from accounts.models import User,OTP
from random import randint
from customer.models import Customer,Payments
from sale.models import Sale
from product.models import Category,AvailableProduct,Product
from django.http import JsonResponse
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


def reports_view(request):
    number_products = Product.objects.filter(user=request.user).count()
    number_products_mojod =  Product.objects.filter(user=request.user,status=True).count()
    number_products_not_mojod =  Product.objects.filter(user=request.user,status=False).count()
    customers = Customer.objects.filter(user=request.user).count()
    sales_user = Customer.objects.filter(user=request.user)
    kharid_user = AvailableProduct.objects.filter(user=request.user)
    sale_price = 0
    kharid_price = 0
    for i in sales_user:
        sale_price += i.price

    for i in kharid_user:
        kharid_price += i.price_kol
    
    customers_not_paid = Customer.objects.filter(user=request.user,is_paid=False).count()
    customers_paid = Customer.objects.filter(user=request.user,is_paid=True).count()
    context = {"kharid_price":kharid_price,"sale_price":sale_price,"number_products" :int(number_products),"number_products_mojod":int(number_products_mojod),"number_products_not_mojod":int(number_products_not_mojod) ,
              "customers":customers,"customers_not_paid":customers_not_paid, "customers_paid":customers_paid}
    return render(request,"accounts/reports.html",context)



