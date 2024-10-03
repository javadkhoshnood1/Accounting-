from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib import messages
# Create your views here.
from .models import Contact


class contact_page_view(TemplateView):
    template_name = "contact/contact.html"

    def post(self,request):
        discription = request.POST.get("discription")
        print(discription)
        messages.success(request,"نظر شما ثبت شد !")
        Contact.objects.create(user=request.user,discription=discription,status=False)
        return redirect("/contact/")
    