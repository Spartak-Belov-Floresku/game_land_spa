# Generated by Django 4.1 on 2022-09-03 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_order_taxprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='ShippingPrice',
        ),
    ]
