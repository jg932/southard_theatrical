from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Garment

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def garments_index(request):
  garments = Garment.objects.all()
  return render(request, 'garments/index.html', { 'garments': garments })

def garments_detail(request, garment_id):
  garment = Garment.objects.get(id=garment_id)
  return render(request, 'garments/detail.html', {'garment': garment })

class GarmentCreate(CreateView):
  model = Garment
  fields = '__all__'