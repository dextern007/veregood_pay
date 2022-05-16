# Generated by Django 3.2.8 on 2022-05-16 16:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0032_alter_wallet_wallet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_id',
            field=models.UUIDField(default=uuid.UUID('8675069b-8b20-4989-9a9e-99aeba7138d1'), unique=True),
        ),
    ]