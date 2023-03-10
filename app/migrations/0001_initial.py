# Generated by Django 4.1.4 on 2022-12-15 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('phone_number', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_people', models.IntegerField(default=0)),
                ('total_price', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.room')),
            ],
        ),
    ]
