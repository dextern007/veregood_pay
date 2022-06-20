# Generated by Django 3.2 on 2022-06-19 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0019_auto_20220619_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='2656', max_length=255),
        ),
        migrations.CreateModel(
            name='VariationGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_price', models.BooleanField(default=False)),
                ('title', models.CharField(choices=[('color', 'color'), ('size', 'size'), ('weight', 'weight')], default='simple', max_length=100)),
                ('suffix', models.CharField(blank=True, max_length=100, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='varation_group', to='veregood.product')),
            ],
        ),
    ]