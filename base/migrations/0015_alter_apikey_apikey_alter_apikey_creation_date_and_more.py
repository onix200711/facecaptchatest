# Generated by Django 5.0.6 on 2024-07-19 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_apikey_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='apikey',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='apikey',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 19, 12, 16, 43, 79239, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='apikey',
            name='expiration_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 18, 12, 16, 43, 79239, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 19, 12, 16, 43, 79239, tzinfo=datetime.timezone.utc)),
        ),
    ]
