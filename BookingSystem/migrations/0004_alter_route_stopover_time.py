# Generated by Django 4.2.1 on 2023-05-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingSystem', '0003_rename_time_zone_airport_time_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='stopover_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
