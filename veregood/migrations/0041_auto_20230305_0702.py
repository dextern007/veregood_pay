# Generated by Django 3.2.12 on 2023-03-05 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0040_auto_20230304_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='7064', max_length=255),
        ),
        migrations.AlterField(
            model_name='productbid',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_bid', to='veregood.product'),
        ),
        migrations.AlterField(
            model_name='productquote',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_quote', to='veregood.product'),
        ),
    ]
