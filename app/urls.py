from django.urls import path
from app import views

urlpatterns = [
    path('', views.buymeWater, name='buymewater'),
    path('support-history/', views.supportHistory, name='supporthistory'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
