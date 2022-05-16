# Generated by Django 3.2.8 on 2022-05-16 15:49

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20220420_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.CharField(default=uuid.uuid4, max_length=255, unique=True)),
                ('address', models.TextField(blank=True, max_length=1000, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Location')),
                ('location_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gst_number', models.CharField(blank=True, max_length=100, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=100, null=True)),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=10)),
                ('commision_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(default=18)),
                ('aadhar_number', models.CharField(blank=True, max_length=100, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=100, null=True)),
                ('store_name', models.CharField(blank=True, max_length=255, null=True)),
                ('store_describtion', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_mobile_number', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_email', models.CharField(blank=True, max_length=255, null=True)),
                ('closed', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
