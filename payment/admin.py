from django.contrib import admin
from .models import BaseModel, Payment
# Register your models here.


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fields = ['user', 'is_paid', 'order_id','amount',
             'status', 'payment_id', 'quantity']