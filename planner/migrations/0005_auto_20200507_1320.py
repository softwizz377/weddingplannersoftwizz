# Generated by Django 2.0 on 2020-05-07 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_auto_20200507_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='bookingfor',
            new_name='Bookingfor',
        ),
    ]
