# Generated by Django 3.2.8 on 2022-05-16 13:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0025_alter_wallet_wallet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_id',
            field=models.UUIDField(default=uuid.UUID('823eeb96-730a-4d0d-8f5f-1e94dc550bd4'), unique=True),
        ),
    ]
