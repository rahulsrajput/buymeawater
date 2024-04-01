from django.urls import path, include
from payment import views

urlpatterns = [
    path('support/', views.support, name='support'),
    path('support-success/', views.supportSuccess, name='supportsuccess'),
]