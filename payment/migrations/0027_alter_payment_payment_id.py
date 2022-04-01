# Generated by Django 3.2.12 on 2022-03-30 19:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0026_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default=uuid.UUID('3aed42f4-7f6f-41d7-8549-71f104de2f31'), max_length=255, unique=True),
        ),
    ]
