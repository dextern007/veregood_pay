# Generated by Django 3.2.12 on 2022-03-25 22:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0013_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default=uuid.UUID('68653bfb-6b60-454e-8ff7-7931a1fd280b'), max_length=255, unique=True),
        ),
    ]
