from django.shortcuts import render


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def garment_index(request):
  return render(request, 'garments/index.html', { 'garments': garments })