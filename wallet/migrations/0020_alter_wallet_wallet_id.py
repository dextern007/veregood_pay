# Generated by Django 3.2.8 on 2022-05-09 21:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0019_alter_wallet_wallet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_id',
            field=models.UUIDField(default=uuid.UUID('ed142dac-68c9-42c0-9348-c0331796c8cf'), unique=True),
        ),
    ]