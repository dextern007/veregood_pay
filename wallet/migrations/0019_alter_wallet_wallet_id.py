# Generated by Django 3.2.8 on 2022-05-09 21:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0018_alter_wallet_wallet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_id',
            field=models.UUIDField(default=uuid.UUID('56489b57-ff21-4e59-8d92-41e5868b99e7'), unique=True),
        ),
    ]