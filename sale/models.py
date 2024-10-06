from django.db import models
from accounts.models import User
from product.models import Product
from customer.models import Customer
# Create your models here.
from jalali_date import datetime2jalali,date2jalali


class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tedad = models.BigIntegerField(default=0)
    price_kol = models.BigIntegerField(default=0)
    created_data = models.DateTimeField(auto_now_add=True,null=True,blank=True, verbose_name="تاریخ اضافه شدن")

    def Created_at(self):
        return date2jalali(self.created_data)

    class Meta:
        verbose_name = "فروش"
        verbose_name_plural = "فروش ها "

        



    