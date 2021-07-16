# Generated by Django 3.2.5 on 2021-07-16 01:12

import autoslug.fields
from django.db import migrations, models
import service.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_auto_20210715_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug_view',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=service.models.image_upload),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=autoslug.fields.AutoSlugField(allow_unicode=True, blank=True, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]