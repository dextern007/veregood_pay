# Generated by Django 3.2.12 on 2022-03-30 15:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0022_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default=uuid.UUID('184d6cd1-2ff5-44c8-bc11-79258db482d5'), max_length=255, unique=True),
        ),
    ]
