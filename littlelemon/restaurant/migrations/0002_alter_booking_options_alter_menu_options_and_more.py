# Generated by Django 4.2.4 on 2023-08-16 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Booking', 'verbose_name_plural': 'Booking Records'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu', 'verbose_name_plural': 'Menu Items'},
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='no_of_guests',
            new_name='number_of_guests',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(),
        ),
    ]
