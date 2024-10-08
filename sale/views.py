from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
# Create your views here.
from django.views.generic import TemplateView
from customer.models  import Customer
from product.models import Product,Category
from sale.models import Sale
class SaleView(TemplateView):
    template_name = 'sale/sale.html'

    def get(self,request):
        search = request.GET.get("search")
        customers = None
        customer = request.GET.get("customer")
        search_products = request.GET.get("search_products")
        products = Product.objects.all().filter(user=request.user).filter(status=True)
        categorys = Category.objects.all().filter(user=request.user)
        if customer:
            customers_list = Customer.objects.filter(user=request.user)
            customer_selected = get_object_or_404(customers_list,id=customer)
            messages.success(request,f"مشتری {customer_selected.fullname} انتخاب شد ")
            return render(request,"sale/sale.html",{"customer_selected":customer_selected,"products":products,"categorys":categorys})
        if search_products:
            customer_id = request.GET.get("customer_selected")
            customers_list = Customer.objects.filter(user=request.user)
            customer_selected = get_object_or_404(customers_list,id=customer_id)
            products = Product.objects.filter(user=request.user).filter(title__contains=search_products)
            return render(request,"sale/sale.html",{"customer_selected":customer_selected,"products":products,"search_products":search_products})

        
        if search:
            customers = Customer.objects.filter(user=request.user).filter(fullname__contains=search)
            if customers:
                messages.success(request,f"تعداد {customers.count()} مشتری یافت شد ! مشتری خود را انتخاب کنید ")
            else:
                messages.error(request,"هیچ مشتری یافت نشد ! مشتری خود را اضافه کنید ")
        return render(request,"sale/sale.html",{"customers" :customers})
    
    def post(self,request):
        products = Product.objects.all().filter(user=request.user).filter(status=True)
        customer = request.POST.get("customer")
        customers_list = Customer.objects.filter(user=request.user)
        customer_selected = get_object_or_404(customers_list,id=customer)
        for item in products :
                products = request.POST.get(f"id-{item.id}")
                tedad = request.POST.get(f"tedad-{item.id}")
                print(tedad,item.mojidi)
                if products:
                    if int(tedad) > item.mojidi:
                        messages.error(request,f"تعداد محصول در خواستی  {item.title} موجود نیست ")
                        return redirect(f"/customers/{customer}")
                    else:
                        new_sale = Sale.objects.create(user=request.user,customer=customer_selected,product=item,tedad=int(tedad))
                        new_sale.price_kol = new_sale.tedad * new_sale.product.price_selling
                        customer_selected.price += new_sale.price_kol
                        customer_selected.price_mandeh += new_sale.price_kol
                        if customer_selected.price_mandeh !=0:
                            customer_selected.is_paid = False
                        new_sale.save()
                        item.mojidi -= int(tedad)
                        item.save()
                        customer_selected.save()
        messages.success(request,"فروش محصول ثبت شد ")
        return redirect(f"/customers/{customer}")
        
        messages.error(request,"هیچ اطلاعاتی دریافت نشد ")
        return redirect(f"/sale/")