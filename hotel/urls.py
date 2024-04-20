from django.urls import path
from rest_framework import routers
from .views import *
router=routers.SimpleRouter()

router.register(r'user',UserProfileViewset,basename='user')
router.register(r'roomtype',RoomtypeViewset,basename='roomtype')
router.register(r'room',RoomViewset,basename='room')
router.register(r'reservation',ReservationViewset,basename='reservation')
router.register(r'staff',StaffViewset,basename='staff')
router.register(r'task',TaskViewset,basename='task')
router.register(r'shift',ShiftViewset,basename='shift')
router.register(r'supplier',SupplierViewset,basename='supplier')
router.register(r'inventoryitem',InventoryItemViewset,basename='invenotryitem')
router.register(r'purchaseorder',PurchaseOrderViewset,basename='purchaseorder')
router.register(r'feedback',FeedbackViewset,basename='Feedback')
router.register(r'invoiceitem',InvoiceItemViewSet,basename='invoiceitem')
router.register(r'payment',PaymentViewSet,basename='payment')
router.register(r'invoice',InvoiceViewset,basename='invoice')
urlpatterns =router.urls+ [
]


