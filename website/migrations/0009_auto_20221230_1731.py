# Generated by Django 3.2.12 on 2022-12-30 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_jsonserializer_api'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsonserializer',
            name='headers',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jsonserializer',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
