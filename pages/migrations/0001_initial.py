# Generated by Django 3.2 on 2022-06-17 07:01

from django.db import migrations, models
import tinymce.models


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
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]
