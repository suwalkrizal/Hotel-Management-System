from django.db import models

# Create your models here.

class Roomtype(models.Model):
    name = models.CharField(max_length=100)
    amenities = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Room(models.Model):
    number = models.CharField(max_length=10)
    room_type = models.ForeignKey(Roomtype, on_delete = models.CASCADE)
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    user = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return self.name


