# Generated by Django 2.0 on 2020-05-07 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='appointmentfor',
            new_name='Bookingfor',
        ),
        migrations.AlterModelTable(
            name='booking',
            table='Booking',
        ),
        migrations.AlterModelTable(
            name='contactus',
            table='ContactUs',
        ),
        migrations.AlterModelTable(
            name='feedback',
            table='Feedback',
        ),
    ]
