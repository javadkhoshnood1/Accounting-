# Generated by Django 5.1.1 on 2024-10-02 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_created_at_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='availableproduct',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
