# Generated by Django 5.0.6 on 2024-07-03 08:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0006_alter_usermodels_email_alter_usermodels_name'),
        ('coupon', '0002_rename_mininum_amount_coupon_minimum_amount'),
        ('products', '0013_alter_variant_slug'),
        ('user_profile', '0003_useraddress_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('payment_method', models.CharField(max_length=20)),
                ('order_status', models.CharField(choices=[('ordered', 'Ordered'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='ordered', max_length=20)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('delivery_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('shipping_charge', models.FloatField(default=0.0)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.useraddress')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coupon.coupon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.usermodels')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.variant')),
            ],
        ),
    ]
