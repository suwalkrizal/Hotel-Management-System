# Generated by Django 5.0.3 on 2024-04-02 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0013_alter_shift_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='shift',
            field=models.CharField(choices=[('morning_sift', 'Morining_shift'), ('day_shift', 'Day_shift'), ('night_shift', 'Nignt_shift')], default='day_shift', max_length=100),
        ),
        migrations.AlterField(
            model_name='shift',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.staff'),
        ),
    ]