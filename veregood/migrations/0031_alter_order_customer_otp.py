# Generated by Django 3.2.12 on 2022-12-30 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0030_alter_order_customer_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='7190', max_length=255),
        ),
    ]
