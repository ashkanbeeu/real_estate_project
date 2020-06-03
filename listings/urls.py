from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name = 'listings_index'),
  path('<int:listing_id>', views.listing, name = 'listings_listing'),
  path('search/', views.search, name = 'listings_search'),
]