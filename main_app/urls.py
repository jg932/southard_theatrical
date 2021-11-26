from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('garments/', views.garments_index, name='garments_index'),
  path('garments/<int:garment_id>/', views.garments_detail, name='garments_detail'),
  path('garments/create/', views.GarmentCreate.as_view(), name='garments_create'),
]