# Generated by Django 4.2.1 on 2023-06-10 23:52

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('BookingSystem', '0002_alter_passenger_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
