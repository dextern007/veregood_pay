# Generated by Django 3.2.8 on 2022-05-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0004_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='veregood/brands/icon'),
        ),
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='veregood/brands/image'),
        ),
    ]
