# Generated by Django 4.1.4 on 2023-01-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_booking_reservation_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='reservation_num',
            field=models.IntegerField(default=0, null=True),
        ),
    ]