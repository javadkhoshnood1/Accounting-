# Generated by Django 5.1.1 on 2024-10-03 04:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_delete_availableproduct'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mojodi', models.PositiveBigIntegerField(default=0, verbose_name='موجودی')),
                ('company', models.CharField(max_length=255, verbose_name='شرکت خرید')),
                ('status', models.BooleanField(default=True)),
                ('discription', models.TextField(blank=True, max_length=300, null=True, verbose_name='توضیحات مدیر')),
                ('price', models.BigIntegerField(blank=True, default=0, null=True, verbose_name='قیمت خرید')),
                ('off', models.IntegerField(blank=True, default=0, null=True, verbose_name='تخفیف  شرکت ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'موجودی محصول',
                'verbose_name_plural': 'موجودی محصولات  ',
            },
        ),
    ]
