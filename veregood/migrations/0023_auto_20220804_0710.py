# Generated by Django 3.2 on 2022-08-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0022_auto_20220804_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='4535', max_length=255),
        ),
        migrations.AlterField(
            model_name='producttab',
            name='content',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
