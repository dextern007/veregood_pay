# Generated by Django 3.2 on 2022-06-17 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0011_alter_order_customer_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='7930', max_length=255),
        ),
    ]
