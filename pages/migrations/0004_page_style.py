# Generated by Django 3.2 on 2022-06-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='style',
            field=models.TextField(blank=True, null=True),
        ),
    ]
