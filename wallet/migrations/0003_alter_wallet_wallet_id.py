# Generated by Django 3.2.12 on 2022-03-30 13:35

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
            field=models.UUIDField(default=uuid.UUID('74c57063-8ccc-4b83-9ed8-b7c3ac8a906a'), unique=True),
        ),
    ]
