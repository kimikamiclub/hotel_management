# Generated by Django 4.1.4 on 2023-01-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_client_id_booking_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
