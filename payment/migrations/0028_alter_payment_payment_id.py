# Generated by Django 3.2.8 on 2022-05-16 13:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0027_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default=uuid.UUID('aee28951-940b-4d60-9c3b-19d7283d0416'), max_length=255, unique=True),
        ),
    ]