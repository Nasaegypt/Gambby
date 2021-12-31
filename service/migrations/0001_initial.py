# Generated by Django 3.2.5 on 2021-11-29 15:34

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import service.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0011_auto_20211129_1734'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('service_type', models.CharField(choices=[('At Home', 'At Home'), ('In Place', 'In Place'), ('Online', 'Online')], max_length=15)),
                ('description', models.TextField(max_length=500)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('availability', models.CharField(choices=[('Active', 'Active'), ('Not Active', 'Not Active')], max_length=10)),
                ('cost', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to=service.models.image_upload)),
                ('slug', autoslug.fields.AutoSlugField(allow_unicode=True, editable=True, populate_from='title', unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_owner', to=settings.AUTH_USER_MODEL)),
                ('service_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.city')),
                ('service_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.country')),
                ('service_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.region')),
            ],
        ),
    ]
