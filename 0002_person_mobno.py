# Generated by Django 3.2.9 on 2021-12-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='mobno',
            field=models.CharField(default='no details', max_length=12),
        ),
    ]
