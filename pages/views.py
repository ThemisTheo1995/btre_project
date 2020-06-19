from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, region_choices
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings_all = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]

    context = {
        'region_choices':region_choices,
        'listings_all': listings_all,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)

def test(request):
    return render(request, 'realtor_email/rent_inquiry.html')
