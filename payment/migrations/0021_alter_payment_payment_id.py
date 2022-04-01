# Generated by Django 3.2.12 on 2022-03-30 14:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0020_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default=uuid.UUID('e1937b1a-905b-465d-ba7c-11ae25c03f65'), max_length=255, unique=True),
        ),
    ]
