# Generated by Django 5.0.6 on 2024-08-02 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_usermodels_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodels',
            name='referral_code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_code', models.CharField(max_length=10, unique=True)),
                ('referred_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referrals', to='authentication.usermodels')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.usermodels')),
            ],
        ),
    ]
