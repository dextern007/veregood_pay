# Generated by Django 3.2 on 2022-08-04 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('symbol', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency', models.CharField(blank=True, max_length=255, null=True)),
                ('to_currency', models.CharField(blank=True, max_length=255, null=True)),
                ('exchange_rate', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
