from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Garment, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'southard-theatrical'

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def garments_index(request):
  garments = Garment.objects.all()
  return render(request, 'garments/index.html', { 'garments': garments })

def garments_detail(request, garment_id):
  garment = Garment.objects.get(id=garment_id)
  return render(request, 'garments/detail.html', {'garment': garment })

def add_photo(request, garment_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, garment_id=garment_id)
      garment_photo = Photo.objects.filter(garment_id=garment_id)
      if garment_photo.first():
        garment_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('garments_detail', garment_id=garment_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('garments_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class GarmentCreate(CreateView):
  model = Garment
  fields = '__all__'
  success_url = '/garments/'

class GarmentUpdate(UpdateView):
  model = Garment
  fields = '__all__'

class GarmentDelete(DeleteView):
  model = Garment
  success_url = '/garments/'

