from django.db import models
from django.urls import reverse


# Create your models here.

class Garment(models.Model):
  type = models.CharField(max_length=250)
  rate = models.CharField(max_length=250)
  color = models.CharField(max_length=250)
  genre = models.CharField(max_length=250)
  sizing = models.CharField(max_length=350)
  materials = models.CharField(max_length=350)
  care = models.TextField(blank=True)
  notes = models.TextField(blank=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('garments_detail', kwargs={'garment_id': self.id})

