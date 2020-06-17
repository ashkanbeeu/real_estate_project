from django.contrib import admin
from .models import Listing

class ListingsAdmin(admin.ModelAdmin):
  list_display = ( 'id', 'title', 'is_published', 'price', 'list_date', 'realtor' )
  list_display_links = ( 'id', 'title' )
  list_filter = ('realtor',)
  search_fields = ('title', 'description')
  list_per_page = 20


admin.site.register(Listing, ListingsAdmin)
