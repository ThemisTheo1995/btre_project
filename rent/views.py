from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, bedroom_choices, region_choices, city_choices, property_type, round_down
from listings.models import Listing
import requests
from urllib.parse import urlencode





GOOGLE_API_KEY = "AIzaSyDTvH62eDRDBLJQSMFReQsIpHXkY29QFcg"

def index(request):
  rent = Listing.objects.order_by('-list_date').filter(is_published=True, is_to_rent = True)
  paginator = Paginator(rent, 3)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'rent': paged_listings,
  }

  return render(request, 'rent/rent.html', context)

def rentlisting(request, rent_id):
  rentlisting = get_object_or_404(Listing, pk=rent_id)
  geo_lat = rentlisting.location[0]
  geo_lng = rentlisting.location[1]

  context = {
    'geo_lat':geo_lat,
    'geo_lng':geo_lng,
    'rentlisting': rentlisting,
  }

  return render(request, 'rent/rentlisting.html', context)

def rentsearch(request):
  queryset_list1 = Listing.objects.order_by('-list_date').filter(is_to_rent=True, is_published=True)
  
    # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list1 = queryset_list1.filter(description__icontains=keywords)

    # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list1 = queryset_list1.filter(city__iexact=city)

    # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list1 = queryset_list1.filter(bedrooms__lte=bedrooms)

    # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list1 = queryset_list1.filter(price__lte=price)

    #Region
  if 'region' in request.GET:
    region = request.GET['region']
    if region:
      queryset_list1 = queryset_list1.filter(region__iexact=region)
  
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
        queryset_list1 = queryset_list1.filter(geo_lat__icontains = geo_lat,geo_lng__icontains=geo_lng) or queryset_list1.filter(city__icontains =city)


  context = {
      'region_choices':region_choices,
      'rent':queryset_list1,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
      'values': request.GET,
      'city_choices':city_choices,
      'property_type': property_type,
  }
  
  return render(request, 'rent/rentsearch.html', context)