# Generated by Django 3.2.5 on 2021-07-30 13:28

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0018_remove_service_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=autoslug.fields.AutoSlugField(allow_unicode=True, blank=True, editable=True, null=True, populate_from='title', unique=True),
        ),
    ]
