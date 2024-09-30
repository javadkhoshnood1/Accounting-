from django.db import models
from jalali_date import datetime2jalali
from accounts.models import User
# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200, null=True, blank=True, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=12, unique=True, verbose_name="شماره تماس")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده ")

    price = models.BigIntegerField(default=0,verbose_name="حساب در فروشگاه")
    discription = models.TextField(max_length=300, null=True, blank=True, verbose_name="توضیحات مدیر")
    created_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ اضافه شدن")
    image = models.ImageField(upload_to="customer/", null=True, blank=True, verbose_name="عکس پروفایل")
    address = models.TextField(null=True,blank=True,verbose_name="ادرس کاربر")


    def Created_at(self):
        return datetime2jalali(self.created_at)

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتری ها  "

    def __str__(self):
        return self.phone
