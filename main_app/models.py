from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

AUTH_USER_MODEL = 'main_app.MyUser'

class MyUser(AbstractUser):
  pass

class Garment(models.Model):
  type = models.CharField
  rate = models.CharField
  color = models.CharField
  genre = models.CharField
  sizing = models.CharField
  materials = models.CharField
  care = models.TextField
  notes = models.TextField