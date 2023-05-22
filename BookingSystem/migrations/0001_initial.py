# Generated by Django 4.2.1 on 2023-05-22 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('time_Zone', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Airport',
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Passenger',
            },
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('plane_id', models.AutoField(primary_key=True, serialize=False)),
                ('seats', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Plane',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('depature_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('stopover_time', models.TimeField(blank=True, null=True)),
                ('arrival_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_location', to='BookingSystem.airport')),
                ('depature_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depature_location', to='BookingSystem.airport')),
                ('stopover_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stopover_location', to='BookingSystem.airport')),
            ],
            options={
                'db_table': 'Route',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('plane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookingSystem.plane')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookingSystem.route')),
            ],
            options={
                'db_table': 'Flight',
            },
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookingSystem.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookingSystem.passenger')),
            ],
            options={
                'db_table': 'Bookings',
            },
        ),
    ]
