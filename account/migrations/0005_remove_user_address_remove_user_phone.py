# Generated by Django 4.2.5 on 2023-09-26 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_shippingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
