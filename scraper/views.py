from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scraper import scrapeAmazon, scrapeFlipkart
# Create your views here.
@api_view(['GET'])
def amazon_scraper(request):
    url = request.query_params.get('item')
    data = scrapeAmazon(url)
    return Response(data)

@api_view(['GET'])
def flipkart_scraper(request):
    url = request.query_params.get('item')
    data = scrapeFlipkart(url)
    return Response(data)

def home(request):
    return render(request, 'index.html')