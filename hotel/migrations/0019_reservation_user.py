# Generated by Django 4.1.6 on 2024-04-07 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0018_remove_reservation_booking_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
