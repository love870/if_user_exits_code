# Generated by Django 3.0.6 on 2022-03-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200611_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
