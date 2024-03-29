# Generated by Django 3.2 on 2022-06-17 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('page_key', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('keyword', models.TextField(blank=True, max_length=5500, null=True)),
                ('description', models.TextField(blank=True, max_length=5500, null=True)),
                ('page', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.page')),
            ],
        ),
    ]
