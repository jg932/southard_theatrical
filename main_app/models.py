from django.db import models


# Create your models here.

class Garment(models.Model):
  type = models.CharField
  rate = models.CharField
  color = models.CharField
  genre = models.CharField
  sizing = models.CharField
  materials = models.CharField
  care = models.TextField
  notes = models.TextField