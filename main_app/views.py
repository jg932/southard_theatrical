from django.shortcuts import render
from .models import Garment

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def garments_index(request):
  garments = Garment.objects.all()
  return render(request, 'garments/index.html', { 'garments': garments })