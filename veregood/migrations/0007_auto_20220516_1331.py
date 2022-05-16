# Generated by Django 3.2.8 on 2022-05-16 13:31

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('veregood', '0006_auto_20220513_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='veregood/brands/icon')),
                ('image', models.ImageField(blank=True, null=True, upload_to='veregood/brands/image')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='veregood.product')),
                ('wishlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wishitem', to='veregood.wishlist')),
            ],
        ),
        migrations.DeleteModel(
            name='ColorVariation',
        ),
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='flat_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='useraddress', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cartitem', to='veregood.cart'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='line_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='veregood.product'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='veregood.cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='coupoun_discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='coupun_applied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_otp',
            field=models.CharField(default='1978', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_charge',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_status_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='final_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.CharField(choices=[('online', 'online'), ('cod', 'cod')], default='onprocess', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('onprocess', 'onprocess'), ('accepted', 'accepted'), ('picked', 'picked'), ('pending', 'pending'), ('abonded', 'abonded'), ('delivered', 'delivered'), ('recieved ', 'recieved'), ('on_the_way', 'on_the_way'), ('recived_by_delivery', 'recived_by_delivery'), ('delayed', 'delayed')], default='onprocess', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='payment',
            name='amount_paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='captured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productlisting',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='veregood.product'),
        ),
        migrations.AddField(
            model_name='variation',
            name='addon_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='variation',
            name='has_price',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='variation',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='variation',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variation', to='veregood.product'),
        ),
        migrations.AddField(
            model_name='variation',
            name='sub_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variation',
            name='text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variation',
            name='value',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variation',
            name='variation_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='veregood.variationtype'),
        ),
        migrations.AddField(
            model_name='variationtype',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='variationtype',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productlisting',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_listing', to='veregood.collection'),
        ),
    ]