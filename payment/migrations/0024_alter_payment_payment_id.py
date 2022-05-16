# Generated by Django 3.2.8 on 2022-05-13 17:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0023_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default=uuid.UUID('4007a758-9d2b-4368-94de-cef377537ff4'), max_length=255, unique=True),
        ),
    ]