# Generated by Django 3.0.6 on 2020-05-26 06:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200525_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]{12}$')]),
        ),
    ]
