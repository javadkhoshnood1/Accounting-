from django.shortcuts import render,redirect
from .models import Customer
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.

def customer_list_view(request):
    customers = Customer.objects.filter(user=request.user)
    search = request.GET.get("search")
    if search:
        customers = Customer.objects.filter(user=request.user).filter(fullname__contains=search)
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        discription = request.POST.get("discription")
        if fullname and phone and discription :
            if Customer.objects.filter(user=request.user).filter(fullname__contains=fullname) or Customer.objects.filter(user=request.user).filter(phone=phone) :
                messages.error(request,"این کاربر در سایت وجود دارد !")
                return render(request,"customer/list.html",{"customers":customers , "search":search})
            else:
                new_customer = Customer.objects.create(phone=phone,user=request.user,fullname=fullname,discription=discription)
                messages.success(request,"مشتری جدید اضافه شد !")
                return redirect(f"/customers/{new_customer.id}")
        else:
            messages.error(request,"اطلاعات مشتری ناقص است !")
            return render(request,"customer/list.html",{"customers":customers , "search":search})

    return render(request,"customer/list.html",{"customers":customers , "search":search})



def customer_detail_view(request,id):
    customers = Customer.objects.filter(user=request.user)
    customer = get_object_or_404(customers, id=id)
    return render(request,"customer/detail.html",{"customer":customer })
