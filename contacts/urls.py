from django.urls import path

from . import views

urlpatterns = [
  path('contact', views.contact, name='contact'),
  path('rent_contact', views.rent_contact,name='rent_contact')
]