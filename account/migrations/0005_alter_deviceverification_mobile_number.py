# Generated by Django 3.2.12 on 2022-04-20 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_deviceverification_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceverification',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
