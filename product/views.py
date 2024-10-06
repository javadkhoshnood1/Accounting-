from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,AvailableProduct,Product
# Create your views here.
from django.contrib import messages


def product_detail_view(request,id):
    products = Product.objects.all().filter(user=request.user) 
    product = get_object_or_404(products,id=id)
    list_kharid_product = AvailableProduct.objects.filter(user=request.user).filter(product=product)
    if product.mojidi != 0 :
        product.status = True
    else:
        product.status = False
    product.sod = product.price_selling - product.price
    product.save()
    if request.method == "POST":
        company = request.POST.get("company")
        mojodi = request.POST.get("mojodi")
        price = request.POST.get("price")
        off = request.POST.get("off")
        discription = request.POST.get("discription")
        if company and mojodi and price and off :
            khrid_jadid = AvailableProduct.objects.create(user=request.user,product=product,company=company,mojodi=int(mojodi),price=int(price),off=int(off),discription=discription)
            product.mojidi += int(mojodi)
            product.price = int(price)
            khrid_jadid.price_kol = int(price) * int(mojodi)
            khrid_jadid.price_kol = khrid_jadid.price_kol - khrid_jadid.price_kol * int(off) /100

            product.price_selling = int(price) + int(price) * product.percent /100
            if product.mojidi != 0:
                product.status = True
            product.sod = product.price_selling - product.price
            product.save()
            khrid_jadid.save()
            messages.success(request,"خرید این حصول انجام شد . ")
            return redirect(f"/products/{product.id}")
    return render(request,"product/detail.html",{"product":product ,"list_kharid_product" :list_kharid_product })




def product_list_view(request):
    categorys = Category.objects.all().filter(user=request.user)
    products = Product.objects.all().filter(user=request.user) 
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        percent = request.POST.get("percent")
        category = request.POST.get("category")
        catgeory_select = get_object_or_404(categorys,id=category)
        
        if title and price and percent and category:
            if Product.objects.filter(user=request.user).filter(title__contains=title):
                messages.error(request,"این محصول در لیست محصولات  وجود دارد !")
                return redirect("/products/")
            else:
                new_product = Product.objects.create(category=catgeory_select,user=request.user,title=title,price=int(price),percent=int(percent))
                new_product.price_selling = int(price) + int(price) * int(percent)/100
                new_product.save()
                messages.success(request,"محصول جدید شما اضافه شد !")
                return redirect(f"/products/{new_product.id}")
        else:
            messages.error(request,"اطلاعات ناقس هست ")
    search = request.GET.get("search")
    if search:
        products = Product.objects.all().filter(user=request.user).filter(title__contains=search)
    return render(request,"product/list.html",{"categorys":categorys,"products":products ,"search":search})


def add_category_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        discription = request.POST.get("discription")
        if title and discription:
            Category.objects.create(user=request.user,title=title,discription=discription)
            messages.success(request,"دسته بندی جدید اضافه شد !")
            return redirect("/products/")
        else:
            messages.error(request,"اطلاعات دریافتی ناقص است !")
            return redirect("/products/")

def category_list_view(request,id):
    categorys = Category.objects.all().filter(user=request.user)
    products = Product.objects.all().filter(user=request.user).filter(category=id)
    name_category = categorys.get(id=id).title
    search = request.GET.get("search")
    if search:
        products = Product.objects.all().filter(user=request.user).filter(title__contains=search)

    return render(request,"product/list.html",{"categorys":categorys,"products":products ,"search":search ,"name_category":name_category})


def delete_product_view(request,id):
    product = Product.objects.get(id=id)
    messages.success(request,f"{product.title} حذف شد !")
    product.delete()
    return redirect("/products/")




