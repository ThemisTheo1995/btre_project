from django.contrib import admin
from .models import Listing
from mapbox_location_field.admin import MapAdmin



class ListingAdmin(MapAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor','is_for_sale','is_to_rent')
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'location', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)







