# Generated by Django 3.0.3 on 2020-03-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
