# Generated by Django 3.2.9 on 2021-12-27 12:29

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211227_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='mydoc',
        ),
        migrations.AddField(
            model_name='person',
            name='mydoc',
            field=models.BooleanField(default=False, verbose_name=django.contrib.auth.models.User),
        ),
    ]
