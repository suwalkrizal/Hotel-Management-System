from rest_framework import  serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        field = (
            'name',
            'number',
            'email',
            'address',
        )
class RoomtypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'category',
            'amenities', 
            'price',
        )
    
        model = Roomtype
        

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'quantity',
            'roomtype',
            'availability'
        )
    
        model = Room  
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
           'user',
           'room',
           'check_in',
           'check_out',
           'room_cost',
        )
    
        model = Reservation
        
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'role',
        )
    
        model =Staff
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'description',
            'assigned_to',
            'completed',
        )
    
        model = Task
        
class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
           'staff',
           'shift',
           'start_time',
           'end_time',
        )
    
        model =Shift
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
          'contact_person',
          'email',
          'phone_number',
        )
    
        model =Supplier
        
class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
          'name',
          'supplier',
          'quantity',
          'reorder_level',
          'unit_price',
        )
    
        model = InventoryItem
        

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
          'inventory_item',
          'quantity_ordered',
          'date_ordered',
        )
    
        model = PurchaseOrder
        
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
          'user',
          'rating',
          'comments',
          'date_submitted',
        )
    
        model = Feedback
        
class InvoiceSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()
    total_paid_amount = serializers.SerializerMethodField()
    balance_due = serializers.SerializerMethodField()
    is_fully_paid = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ['id', 'user', 'date_created', 'due_date', 'is_paid', 'total_amount', 'total_paid_amount', 'balance_due', 'is_fully_paid']

    def get_total_amount(self, obj):
        return sum(item.total_amount() for item in obj.items.all())

    def get_total_paid_amount(self, obj):
        return sum(payment.amount for payment in obj.payments.all())

    def get_balance_due(self, obj):
        return self.get_total_amount(obj) - self.get_total_paid_amount(obj)

    def get_is_fully_paid(self, obj):
        return self.get_balance_due(obj) == 0
    
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'invoice',
            'date_paid',
            'amount',
            'payment_method',
        )
        
class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = (
            'invoice',
            'description', 
            'quantity',
            'unit_price',
            'total_amount',
        )
        
        
