# Generated by Django 3.2.8 on 2022-05-16 15:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0030_alter_wallet_wallet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_id',
            field=models.UUIDField(default=uuid.UUID('ff7495fb-e65b-4f09-bfe9-a9a355dc6a0b'), unique=True),
        ),
    ]