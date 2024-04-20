# Generated by Django 4.1.6 on 2024-04-07 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0017_remove_invoice_total_amount_invoice_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='booking',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='is_cancelled',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='tax_amount',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='room',
            name='number',
        ),
        migrations.AddField(
            model_name='reservation',
            name='check_in',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.room'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]