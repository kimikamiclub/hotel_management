# Generated by Django 4.1.4 on 2023-01-20 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_hotel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='client_id',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='room_id',
            new_name='room',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='hotel_id',
            new_name='hotel',
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
