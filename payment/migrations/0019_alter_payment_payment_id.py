# Generated by Django 3.2.8 on 2022-05-09 21:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0018_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default=uuid.UUID('dafdebea-ff23-4e51-a144-eaf368b6a121'), max_length=255, unique=True),
        ),
    ]