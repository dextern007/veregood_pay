# Generated by Django 3.2.12 on 2022-03-25 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0005_auto_20220325_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileRecharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.service')),
            ],
        ),
    ]
