# Generated by Django 3.2 on 2022-08-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0025_alter_order_customer_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_reference_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='2553', max_length=255),
        ),
    ]
