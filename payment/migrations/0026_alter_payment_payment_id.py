# Generated by Django 3.2.8 on 2022-05-16 13:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0025_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default=uuid.UUID('a4ada2f4-9761-4fdd-b574-4c3c86580791'), max_length=255, unique=True),
        ),
    ]
