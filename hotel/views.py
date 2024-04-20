from .serializer import *
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters import rest_framework as filter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse
from .permission import isFront_DeskorReadOnly, isManagementorReadOnly, isGuestorReadOnly,isAdminorReadOnly



class UserProfileViewset(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields = ('name','number','email','address')
    search_fields=('name',)

class RoomtypeViewset(viewsets.ModelViewSet):
    queryset=Roomtype.objects.all()
    serializer_class=RoomtypeSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields = ('category','amenities')
    search_fields=('category',)

class RoomViewset(viewsets.ModelViewSet):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields = ('quantity','roomtype','availability')
    search_fields=('quantity',)
    
class ReservationViewset(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields = ('user','room','check_in','check_out','room_cost''category','amenities')
    search_fields=('user',)
    
class StaffViewset(viewsets.ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class=StaffSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields = ('name','role')
    search_fields=('name',)
    
class TaskViewset(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields = ('description','assigned_to','completed')
    search_fields=('description',)
    
class ShiftViewset(viewsets.ModelViewSet):
    queryset=Shift.objects.all()
    serializer_class=ShiftSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields = ('staff','shift','start_time','end_time')
    search_fields=('staff',)
    
class SupplierViewset(viewsets.ModelViewSet):
    queryset=Supplier.objects.all()
    serializer_class=SupplierSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields = ('contact_person','email','phone_number')
    search_fields=('contact_person',)
    
class InventoryItemViewset(viewsets.ModelViewSet):
    queryset=InventoryItem.objects.all()
    serializer_class=InventoryItemSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields = ('name','supplier','quantity','reorder_level','unit_price')
    search_fields=('name',)
    
class PurchaseOrderViewset(viewsets.ModelViewSet):
    queryset=PurchaseOrder.objects.all()
    serializer_class=PurchaseOrderSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields = ('inventory_item','quantity_ordered','date_ordered')
    search_fields=('inventory_item',)
    
class FeedbackViewset(viewsets.ModelViewSet):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields = ('user','rating','comments','date_submitted')
    search_fields=('user',)
    
class InvoiceViewset(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('id')
    serializer_class = InvoiceSerializer
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter, filter.DjangoFilterBackend)
    filterset_fields = ('user', 'is_paid')
    search_fields = ('user',)
    permission_classes = [isAdminorReadOnly]


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter, filter.DjangoFilterBackend)
    filterset_fields = ('invoice', 'date_paid', 'quantity',)
    search_fields = ('invoice',)
    
class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,filter.DjangoFilterBackend)
    filterset_fields = ('invoice', 'quantity', 'unit_price',)
    search_fields = ('invoice',)
    
