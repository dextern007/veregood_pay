# Generated by Django 3.2.12 on 2022-03-31 12:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0029_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default=uuid.UUID('1a1459d2-cb1f-41b7-8881-304463eb1054'), max_length=255, unique=True),
        ),
    ]
