# Generated by Django 3.0.7 on 2020-12-06 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mobile_number', models.BigIntegerField(blank=True)),
                ('img_link', models.URLField(blank=True, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', max_length=5000)),
                ('shop_type', models.TextField(blank=True, max_length=1000)),
                ('official_doc_link', models.URLField(blank=True, max_length=5000)),
                ('lane_no', models.TextField(blank=True, max_length=50)),
                ('landmark', models.TextField(blank=True, max_length=1000)),
                ('village', models.TextField(blank=True, max_length=100)),
                ('district', models.TextField(blank=True, max_length=100)),
                ('state', models.TextField(blank=True, max_length=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BuyerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mobile_number', models.BigIntegerField()),
                ('img_link', models.URLField(blank=True, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', max_length=5000)),
                ('lane_no', models.TextField(blank=True, max_length=50)),
                ('landmark', models.TextField(blank=True, max_length=1000)),
                ('village', models.TextField(blank=True, max_length=100)),
                ('district', models.TextField(blank=True, max_length=100)),
                ('state', models.TextField(blank=True, max_length=100)),
                ('pro_user', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BuyerOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed', models.DateTimeField(auto_now_add=True)),
                ('order_sat', models.TextField(max_length=1000)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
