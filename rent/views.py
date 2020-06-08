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
