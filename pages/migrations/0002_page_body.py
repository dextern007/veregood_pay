# Generated by Django 3.2 on 2022-06-17 08:53

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='body',
            field=tinymce.models.HTMLField(default='h'),
            preserve_default=False,
        ),
    ]
