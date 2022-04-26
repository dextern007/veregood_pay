# Generated by Django 3.2.12 on 2022-04-20 11:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_alter_wallet_wallet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_id',
            field=models.UUIDField(default=uuid.UUID('db30f450-1224-4042-942f-dbb13fc3744d'), unique=True),
        ),
    ]
