# Generated by Django 5.0.3 on 2024-04-18 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0033_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='name',
        ),
    ]
