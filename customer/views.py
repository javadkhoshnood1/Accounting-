from django.shortcuts import render,redirect
from .models import Customer,Payments
from django.shortcuts import get_object_or_404
from django.contrib import messages
from sale.models import Sale
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
    print(customers)
    return render(request,"customer/list.html",{"customers":customers , "search":search})



def customer_detail_view(request,id):
    customers = Customer.objects.filter(user=request.user)
    customer = get_object_or_404(customers, id=id)
    customer_sales = Sale.objects.filter(user=request.user).filter(customer=customer)
    if customer.price_mandeh == 0:
        customer.is_paid = True
        customer.save()
    else:
        customer.is_paid =False
        customer.save()
    payments = Payments.objects.filter(user=request.user).filter(customer=customer)
    if request.method == "POST":
        discription = request.POST.get("discription")
        address = request.POST.get("address")
        if address and discription :
            customer.discription = discription
            customer.address = address
            customer.save()
            messages.success(request,"ویرایش اطلاعات انجام شد !")
            return redirect(f"/customers/{customer.id}")
        else:
            messages.error(request,"اطلاعات دریافتی ناقص است !")
            return redirect(f"/customers/{customer.id}")

    return render(request,"customer/detail.html",{"customer":customer ,"payments":payments ,"customer_sales":customer_sales })


def customer_delete_view(request,id):
    customer = Customer.objects.get(id=id)
    if customer:
        customer_sales = Sale.objects.filter(user=request.user).filter(customer=customer)
        customer_sales.delete()
        customer.delete()
        messages.success(request,"مشتری حذف شد !")
    else:
        messages.error(request,"مشتری وجود ندارد !")
        return redirect("/customers/")

    return redirect("/customers/")


def customer_edit_price_view(request,id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        price_paid = request.POST.get("price_paid")
        discription = request.POST.get("discription")
        if  price_paid:
            if int(price_paid) > customer.price_mandeh :
                messages.error(request,f"حداکثر پرداختی باید {customer.price_mandeh}تومان باشد ")
                return redirect(f"/customers/{customer.id}")
            else:
                customer.price_paid_all = customer.price_paid_all + int(price_paid)
                customer.price_mandeh = customer.price - customer.price_paid_all
                if customer.price_mandeh == 0:
                    customer.is_paid = True 
                else:
                    customer.is_paid = False 

                if int(price_paid) != 0:
                    payment_customer =Payments.objects.create(user=request.user,customer=customer,discription=discription)
                    payment_customer.price_paid = int(price_paid)
                    payment_customer.save()
                customer.save()
                messages.success(request,"حساب مشتری شما ویرایش شد !")
                return redirect(f"/customers/{customer.id}") 
        
    
def customer_delete_price_view(request,id):
    customer = Customer.objects.get(id=id)
    payment_customer =Payments.objects.all().filter(user=request.user,customer=customer)
    customer_sales = Sale.objects.filter(user=request.user).filter(customer=customer)
    customer_sales.delete()
    customer.price = 0
    customer.price_mandeh = 0
    customer.price_paid_all = 0
    customer.is_paid = True
    payment_customer.delete()
    customer.save()
    messages.success(request,f"اطلاعات حساب {customer.fullname}ریست شد ! ")
    return redirect(f"/customers/{customer.id}") 


