from django.urls import path
from . import views


urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('garments/', views.garments_index, name='garments_index'),
  path('garments/<int:garment_id>/', views.garments_detail, name='garments_detail'),
  path('garments/create/', views.GarmentCreate.as_view(), name='garments_create'),
  path('garments/<int:pk>/update/', views.GarmentUpdate.as_view(), name="garments_update"),
  path('garments/<int:pk>/delete', views.GarmentDelete.as_view(), name='garments_delete'),
  path('garments/<int:garment_id>/add_photo/', views.add_photo, name='add_photo'),
]