# Generated by Django 3.2 on 2022-07-26 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0016_alter_order_customer_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='9053', max_length=255),
        ),
    ]
