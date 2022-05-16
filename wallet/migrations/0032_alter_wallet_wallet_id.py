# Generated by Django 3.2.8 on 2022-05-16 15:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0031_alter_wallet_wallet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_id',
            field=models.UUIDField(default=uuid.UUID('24482c24-5053-4c6d-9b2a-94da6019db70'), unique=True),
        ),
    ]
