# Generated by Django 3.2 on 2022-06-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]