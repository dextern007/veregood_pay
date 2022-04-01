# Generated by Django 3.2.12 on 2022-03-30 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20220325_2330'),
        ('mobile_recharge', '0003_recharge_mobile_recharge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recharge',
            name='mobile_recharge',
        ),
        migrations.RemoveField(
            model_name='recharge',
            name='recharge_number',
        ),
        migrations.AddField(
            model_name='recharge',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recharge',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recharge',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
        migrations.AddField(
            model_name='recharge',
            name='subscriber_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
