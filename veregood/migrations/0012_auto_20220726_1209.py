# Generated by Django 3.2 on 2022-07-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0011_auto_20220726_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('INR', 'INR'), ('USD', 'USD'), ('EUR', 'EUR')], default='USD', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='7058', max_length=255),
        ),
    ]
