# Generated by Django 3.2.8 on 2022-04-26 12:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default=uuid.UUID('a7e3f1c7-090a-427d-9ef2-7b99a1701c7c'), max_length=255, unique=True),
        ),
    ]
