# Generated by Django 2.0 on 2020-05-07 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_auto_20200507_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Bookingfor',
            new_name='bookingfor',
        ),
    ]