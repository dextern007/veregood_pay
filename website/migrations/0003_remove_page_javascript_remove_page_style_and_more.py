# Generated by Django 4.1.1 on 2022-11-29 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_cascadestyle_javascript_meta_api_key_page_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='javascript',
        ),
        migrations.RemoveField(
            model_name='page',
            name='style',
        ),
        migrations.AddField(
            model_name='cascadestyle',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.page'),
        ),
        migrations.AddField(
            model_name='javascript',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.page'),
        ),
        migrations.AlterField(
            model_name='page',
            name='meta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.meta'),
        ),
    ]
