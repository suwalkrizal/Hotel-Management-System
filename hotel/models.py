from django.db import models
from django.contrib.auth.models import User
from datetime import time,date
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.models import AbstractUser
from register.models import User

# class User(AbstractUser):
#    ROLE_CHOICES = [
#         ('front_desk','Front_Desk'),
#         ('management','Management'),
#         ('guest','Guest'),
#         ('admin','Admin'),
#     ]
   
#    role = models.CharField(max_length=15,choices=ROLE_CHOICES,null=True,blank=True)

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    number =models.CharField( max_length=10)
    email = models.EmailField( max_length=50)
    address = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

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
    quantity = models.PositiveIntegerField(default=1)
    roomtype = models.ForeignKey(Roomtype, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.roomtype.category}-{self.quantity}"
    
class Staff(models.Model):
    ROLE_CHOICES = [
        ('front_desk','Front_Desk'),
        ('management','Management'),
        ('admin','Admin'),
    ]
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=15,choices=ROLE_CHOICES,null=True,blank=True)


    def __str__(self):
        return self.name




class Reservation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null= True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)  # Change the default value as per your requirements
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)  
    room_cost = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)

    def total_amount(self):
        if self.room_cost is not None:
            return self.room_cost, self.user.name
        else:
            return 0, ""

    
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
    start_time = models.TimeField( auto_now=False, auto_now_add=False)
    end_time = models.TimeField( auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.staff.name}-{self.start_time}-{self.end_time}"
    
    
class Supplier(models.Model):
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.contact_person}-{self.email}-{self.phone_number}"
    
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
        return f"{self.inventory_item.name}-{self.quantity_ordered}-{self.date_ordered}"
    
    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comments = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.rating}-{self.comments}-{self.date_submitted}"
    
    
class Invoice(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)   
    date_created=models.DateTimeField(default=timezone.now) 
    due_date=models.DateField()
    is_paid=models.BooleanField(default=False)
    
    def total_amount(self):
        return sum(item.total_amount()for item in self.items.all())
    
    
    def total_paid_amount(self):
        return sum(payment.amount for payment in self.payments.all())
    
    def balance_due(self):
        return self.total_amount() - self.total_paid_amount()

    def is_fully_paid(self):
        return self.balance_due() == 0
    
    def __str__(self):
        return f"Invoice #{self.pk} - {self.user} - Total: {self.total_amount()} - Due: {self.due_date}"
    
class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='payments', on_delete=models.CASCADE)
    date_paid = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment for Invoice #{self.invoice.pk} - {self.amount} - Method: {self.payment_method}" 

    
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_amount(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.description} - Quantity: {self.quantity} - Total: {self.total_amount()}"
    
    
    
# class Invoice(models.Model):
#     reservation = models.ForeignKey(Reservation, on_delete = models.CASCADE)
    
#     total_amount = models.DecimalField(max_digits=10, decimal_places= 2)
#     tax_amount = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Invoice for Reservation ID: {self.reservation.id}"


