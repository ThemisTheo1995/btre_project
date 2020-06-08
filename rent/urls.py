from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='rent'),
    path('<int:rent_id>', views.rentlisting, name='rentlisting'),

]