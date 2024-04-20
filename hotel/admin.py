from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name','number','email','address')
 
@admin.register(Roomtype)
class RoomtypeAdmin(admin.ModelAdmin):
    list_display = ('category','amenities','price')
    search_fields = ('category','price')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('quantity','roomtype','availability')
    

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user','room','check_in','check_out','room_cost')
    
@admin.register(Staff)
class StaffAdmin (admin.ModelAdmin):
    list_display = ('name','role')
    
@admin.register(Task)
class TaskAdmin (admin.ModelAdmin):
    list_display = ('description','assigned_to','completed')
    
@admin.register(Shift)
class ShiftAdmin (admin.ModelAdmin):
    list_display = ('staff','shift','start_time','end_time')


@admin.register(Supplier)
class SupplierAdmin (admin.ModelAdmin):
    list_display = ('contact_person','email','phone_number')
    

@admin.register(InventoryItem)
class InventoryItemAdmin (admin.ModelAdmin):
    list_display = ('name','supplier','quantity','reorder_level','unit_price')
    

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin (admin.ModelAdmin):
    list_display = ('inventory_item','quantity_ordered','date_ordered')
    
@admin.register(Feedback)
class FeedbackAdmin (admin.ModelAdmin):
    list_display = ('user','rating','comments','date_submitted')
    

class PaymentInline(admin.TabularInline):
    model = Payment

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    
    
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline, PaymentInline]
    list_display = ['id', 'user', 'date_created', 'due_date', 'total_paid_amount', 'balance_due', 'is_fully_paid']
    list_filter = ['is_paid']
    search_fields = ['user__name']
    
@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'description', 'quantity', 'unit_price', 'total_amount']
    list_filter = ['invoice']
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'date_paid', 'amount', 'payment_method']
    list_filter = ['invoice__user']

    

    
    