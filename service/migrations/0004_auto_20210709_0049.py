# Generated by Django 3.2.5 on 2021-07-08 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_service_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='availability',
            field=models.CharField(choices=[('Active', 'Active'), ('Not Active', 'Not Active')], default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
