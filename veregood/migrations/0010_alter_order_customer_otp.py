# Generated by Django 3.2 on 2022-07-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0009_auto_20220722_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='5470', max_length=255),
        ),
    ]