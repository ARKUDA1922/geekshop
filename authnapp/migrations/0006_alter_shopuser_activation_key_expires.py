# Generated by Django 3.2.12 on 2022-05-06 20:15

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0005_create_profiles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 5, 8, 20, 15, 30, 201543, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
    ]