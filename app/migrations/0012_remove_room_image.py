# Generated by Django 4.1.4 on 2023-01-27 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_client_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='image',
        ),
    ]
