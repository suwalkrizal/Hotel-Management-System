from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class Roomtype(models.Model):
    Category_choices = [
        ('Standard', 'Standard'),
        ('Deluxe', 'Deluxe'),
        ('Suite', 'Suite'),
    ]
    Amenities_choices = [
        ('Standard', 'One bed room, fan, attached bathroom'),
        ('Deluxe', 'One or double bed room, AC room, attached bathroom, dining room'),
        ('Suite', 'One or double bed room, AC room, attached bathroom, dining room, guest room, gym'),
    ]
    category = models.CharField(max_length=10, choices=Category_choices)
    amenities = models.CharField(max_length=100, choices=Amenities_choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.category
    
class Room(models.Model):
    number = models.CharField(max_length=10)
    roomtype = models.ForeignKey(Roomtype, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.number
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Change the default value as per your requirements
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.room.number} - {self.check_in} to {self.check_out}"

class Reservation(models.Model):
    booking = models.ForeignKey(Booking, on_delete = models.CASCADE)
    is_cancelled = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank = True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.total_amount or not self.tax_amount:
            total_amount = self.room.roomtype.price * (self.check_out - self.check_in).days
            self.total_amount = total_amount
            self.tax_amount = total_amount * 0.1
            
        super().save(*args, **kwargs)
        

        

    
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choice = [
        ('front_desk','Front_Desk'),
        ('housekeeping','Housekeeping'),
        ('management','Management'),
    ]
    role = models.CharField(max_length=50, choices=role_choice)

    def __str__(self):
        return f"{self.user}-{self.role}"
    
class Task(models.Model):
    description = models.TextField()
    assigned_to = models.ForeignKey(Staff, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description}-{self.assigned_to}-{self.completed}"
    
class Shift(models.Model):
    SHIFT_CHOICE = [
        ('morning_sift','Morining_shift'),
        ('day_shift','Day_shift'),
        ('night_shift','Nignt_shift'),
    ]
    staff = models.ForeignKey(Staff, on_delete= models.CASCADE)
    shift = models.CharField(max_length=100, choices=SHIFT_CHOICE, default='day_shift')
    start_time = models.DateField()
    end_time = models.DateField()

    def __str__(self):
        return f"{self.staff}-{self.start_time}-{self.end_time}"
    
    
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}-{self.contact_person}-{self.email}-{self.phone_number}"
    
class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete =models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    reorder_level = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
            
    def __str__(self):
        return f"{self.name}-{self.supplier}-{self.quantity}-{self.reorder_level}-{self.unit_price}"

class PurchaseOrder(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete = models.CASCADE)
    quantity_ordered = models.PositiveIntegerField()
    date_ordered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.inventory_item}-{self.quantity_ordered}-{self.date_ordered}"
    
    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comments = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.rating}-{self.comments}-{self.date_submitted}"
    
class Invoice(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete = models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places= 2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice for Reservation ID: {self.reservation.id}"


