# Generated by Django 3.2 on 2022-06-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0009_alter_order_customer_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='6227', max_length=255),
        ),
    ]