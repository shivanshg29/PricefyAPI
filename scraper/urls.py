from django.urls import path
from .views import amazon_scraper, flipkart_scraper,home

urlpatterns = [
    path('',home,name='home'),
    path('amazon/', amazon_scraper, name='amazon-scraper'),
    path('flipkart/', flipkart_scraper, name='flipkart-scraper'),
]
