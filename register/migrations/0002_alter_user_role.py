# Generated by Django 5.0.3 on 2024-04-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('front_desk', 'Front_Desk'), ('management', 'Management'), ('guest', 'Guest'), ('admin', 'Admin')], default='guest', max_length=15),
        ),
    ]
