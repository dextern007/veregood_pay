# Generated by Django 3.2.12 on 2022-03-30 19:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0014_alter_wallet_wallet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_id',
            field=models.UUIDField(default=uuid.UUID('97067912-28d7-4fdd-96eb-40d98bca6238'), unique=True),
        ),
    ]
