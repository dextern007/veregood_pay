# Generated by Django 3.2 on 2022-06-19 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0027_auto_20220619_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_category_product', to='veregood.maincategory'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='5032', max_length=255),
        ),
    ]