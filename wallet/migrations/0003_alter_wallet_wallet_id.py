# Generated by Django 3.2.8 on 2022-04-15 14:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_alter_wallet_wallet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_id',
            field=models.UUIDField(default=uuid.UUID('bfde7a07-4abb-439d-b609-6bab52bdff95'), unique=True),
        ),
    ]
