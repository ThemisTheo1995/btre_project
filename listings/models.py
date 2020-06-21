from django.db import models
from datetime import datetime
from realtors.models import Realtor
from django.contrib.postgres.fields import ArrayField
from .choices import city_model, region_model







class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100, choices=city_model)
  region = models.CharField(max_length=100,choices=region_model,default='Attica')
  zipcode = models.CharField(max_length=20)
  location = models.TextField()
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  is_for_sale = models.BooleanField(default=False)
  is_to_rent = models.BooleanField(default=False)
  lat = models.DecimalField(max_digits=9, decimal_places=7)
  lng = models.DecimalField(max_digits=9, decimal_places=7)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title
