# Generated by Django 3.2 on 2022-06-16 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0005_auto_20220616_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='4224', max_length=255),
        ),
    ]