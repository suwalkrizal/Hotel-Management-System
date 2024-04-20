# Generated by Django 5.0.3 on 2024-04-04 16:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0016_reservation_tax_amount_reservation_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]