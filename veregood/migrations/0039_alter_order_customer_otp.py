# Generated by Django 3.2 on 2022-06-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0038_auto_20220621_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='6005', max_length=255),
        ),
    ]
