from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, region_choices, city_choices
from django.http import HttpResponse
from .models import Listing
import json



def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True, is_for_sale = True)

  paginator = Paginator(listings, 3)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings,
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  geo_lat = listing.location[0]
  geo_lng = listing.location[1]

  context = {
    'geo_lat':geo_lat,
    'geo_lng':geo_lng,
    'listing': listing,
  
    
  }

  return render(request, 'listings/listing.html', context)

def salesearch(request):
  queryset_list = Listing.objects.order_by('-list_date').filter(is_for_sale=True)
  
  
  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__icontains=city)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)
      
  #Region
  if 'region' in request.GET:
    region = request.GET['region']
    if region:
      queryset_list = queryset_list.filter(region__iexact=region)

    # Location
  if 'location' in request.GET:
    location = request.GET['location']
    if location:
      queryset_list = queryset_list.filter(location__icontains=location)

  context = {
    
    'region_choices':region_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'city_choices':city_choices,
    'values': request.GET,
  }

  return render(request, 'listings/salesearch.html', context)
  return



