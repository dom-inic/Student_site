# Generated by Django 3.0.3 on 2020-03-22 13:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('megapp', '0005_auto_20200322_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(default=datetime.datetime(2020, 3, 22, 13, 9, 56, 271433, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
    ]