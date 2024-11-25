from django.urls import path
from .views import amazon_scraper, flipkart_scraper,home,detect_logo_and_objects_view

urlpatterns = [
    path('',home,name='home'),
    path('amazon/', amazon_scraper, name='amazon-scraper'),
    path('flipkart/', flipkart_scraper, name='flipkart-scraper'),
    path('detect/',detect_logo_and_objects_view,name="detect")
]
