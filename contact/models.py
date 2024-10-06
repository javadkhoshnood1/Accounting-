from django.db import models
from accounts.models import User
from jalali_date import datetime2jalali


class Contact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    discription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ اضافه شدن")
    status = models.BooleanField(default=False)


    
    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def created_date(self):
        return datetime2jalali(self.created_at)