# Generated by Django 3.2 on 2022-06-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='2604', max_length=255),
        ),
    ]
