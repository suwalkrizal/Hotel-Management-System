from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Roomtype)
class RoomtypeAdmin(admin.ModelAdmin):
    list_display = ('category','amenities','price')
    search_fields = ('category','price')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number','availability')
    

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user','check_in','check_out')
    
    
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('booking','is_cancelled')
    
@admin.register(Staff)
class StaffAdmin (admin.ModelAdmin):
    list_display = ('user','role')
    
@admin.register(Task)
class TaskAdmin (admin.ModelAdmin):
    list_display = ('description','assigned_to','completed')
    
@admin.register(Shift)
class ShiftAdmin (admin.ModelAdmin):
    list_display = ('staff','shift','start_time','end_time')


@admin.register(Supplier)
class SupplierAdmin (admin.ModelAdmin):
    list_display = ('name','contact_person','email','phone_number')
    

@admin.register(InventoryItem)
class InventoryItemAdmin (admin.ModelAdmin):
    list_display = ('name','supplier','quantity','reorder_level','unit_price')
    

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin (admin.ModelAdmin):
    list_display = ('inventory_item','quantity_ordered','date_ordered')
    
@admin.register(Feedback)
class FeedbackAdmin (admin.ModelAdmin):
    list_display = ('user','rating','comments','date_submitted')
    
@admin.register(Invoice)
class InvoiceAdmin (admin.ModelAdmin):
    list_display = ('reservation','total_amount','tax_amount')