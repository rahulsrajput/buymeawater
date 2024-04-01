import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Payment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='payments')
    amount = models.DecimalField(null=True, blank=True, max_digits = 15, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=500)
    payment_id = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    # instamojo_response = models.TextField(null=True, blank=True)
