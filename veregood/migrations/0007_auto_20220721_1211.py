# Generated by Django 3.2 on 2022-07-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veregood', '0006_auto_20220720_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='variation',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ManyToManyField(blank=True, to='veregood.Variation'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='3914', max_length=255),
        ),
    ]
