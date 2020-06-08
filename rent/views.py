from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, bedroom_choices, state_choices

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

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list1 = queryset_list1.filter(state__iexact=state)

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

  context = {
      'rent':queryset_list1,
      'state_choices': state_choices,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
      'values': request.GET
  }
  
  return render(request, 'rent/rentsearch.html', context)