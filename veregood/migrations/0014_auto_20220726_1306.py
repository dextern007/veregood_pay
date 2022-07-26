# Generated by Django 3.2 on 2022-07-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0013_alter_order_customer_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='veregood/collection/icon'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='veregood/collection/image'),
        ),
        migrations.AlterField(
            model_name='collectiongroup',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='veregood/collection/group/icon'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='9489', max_length=255),
        ),
    ]