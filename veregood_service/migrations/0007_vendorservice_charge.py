# Generated by Django 3.2.8 on 2022-05-01 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood_service', '0006_auto_20220426_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorservice',
            name='charge',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
