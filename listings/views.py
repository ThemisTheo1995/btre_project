from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, region_choices, city_choices,property_type,round_down
from .models import Listing
import requests
from urllib.parse import urlencode

GOOGLE_API_KEY = "AIzaSyDTvH62eDRDBLJQSMFReQsIpHXkY29QFcg"

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

def salesearch(request, data_type = 'json'):
  queryset_list = Listing.objects.order_by('-list_date').filter(is_for_sale=True, is_published=True)

    #Region
  if 'region' in request.GET:
    region = request.GET['region']
    if region:
      queryset_list = queryset_list.filter(region__iexact=region)

    # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

    # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)
  
    # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # Location
  if 'location' in request.GET:
    location = request.GET['location']
    if len(location)>0: 
    # geocoding API
      endpoint = f"https://maps.googleapis.com/maps/api/geocode/json"
      params = {"address": location, "key": GOOGLE_API_KEY}
      url_params = urlencode(params)
      url = f"{endpoint}?{url_params}"
      r = requests.get(url)
      if r.status_code not in range(200, 299): 
          return {}
      # Combined data
      latlng = r.json()['results'][0]['geometry']['location']
      city = r.json()['results'][0]['address_components'][0].get('long_name')
      #breakdown
      geo_lat = round_down(latlng.get("lat"),1)
      geo_lng = round_down(latlng.get("lng"),1)
      geo_latlng = "{},{}".format(geo_lng,geo_lat)
    # end of geocoding API
    
      if location:
        queryset_list = queryset_list.filter(geo_lat__icontains = geo_lat,geo_lng__icontains=geo_lng) or queryset_list.filter(city__icontains=city)


  context = {
    'listings': queryset_list,
    'values': request.GET,
    'city_choices':city_choices,
    'property_type': property_type,
    'bedroom_choices':bedroom_choices,
    'region_choices':region_choices,
    'price_choices':price_choices,
  }

  return render(request, 'listings/salesearch.html', context)
  



