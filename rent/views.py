from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, bedroom_choices, region_choices, city_choices
from listings.models import Listing




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

  context = {
    'rentlisting': rentlisting,
  }

  return render(request, 'rent/rentlisting.html', context)



def rentsearch(request):
  queryset_list1 = Listing.objects.order_by('-list_date').filter(is_to_rent=True)
  
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

  # Location
  if 'location' in request.GET:
    location = request.GET['location']
    if location:
      queryset_list1 = queryset_list1.filter(location__icontains=location)

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

  context = {
      'region_choices':region_choices,
      'rent':queryset_list1,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
      'values': request.GET,
      'city_choices':city_choices,
  }
  
  return render(request, 'rent/rentsearch.html', context)