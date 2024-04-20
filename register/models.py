from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class User(AbstractUser):
    ROLE_CHOICES = [
        ('front_desk','Front_Desk'),
        ('management','Management'),
        ('guest','Guest'),
        ('admin','Admin'),
    ]

    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='guest')
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='log_user_groups',  # Unique related_name
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='log_user_permissions',  # Unique related_name
        related_query_name='user',
    )

    class Meta:
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Staff(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE, default=1)
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('on_leave', 'On Leave'),
    ]
    availability = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES, default='available')
    
    contact_info = models.CharField(max_length=10, validators=[
        RegexValidator(regex='^[0-9]{10}$', message='Contact information must be a 10-digit number.', code='invalid_contact_information')
    ])

    def __str__(self):
        return f"{self.user.username}-{self.availability}"

