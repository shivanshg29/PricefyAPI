from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pathlib import Path
from .scraper import scrapeAmazon, scrapeFlipkart
from .object import detect_logo_and_objects

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

@api_view(['POST'])
def detect_logo_and_objects_view(request):
    # Ensure the request has an image file
    if 'image' not in request.FILES:
        return Response({"error": "No image file provided."}, status=400)

    # Get the uploaded file
    uploaded_file = request.FILES['image']

    # Save the file temporarily
    temp_dir = Path('temp_images')  # Directory for temporary files
    temp_dir.mkdir(exist_ok=True)  # Create if it doesn't exist
    temp_file_path = temp_dir / uploaded_file.name

    with open(temp_file_path, 'wb+') as temp_file:
        for chunk in uploaded_file.chunks():
            temp_file.write(chunk)

    # Call the detect_logo_and_objects function
    result=[]
    try:
        result=detect_logo_and_objects(str(temp_file_path))
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    finally:
        # Cleanup: Delete the temporary file after processing
        temp_file_path.unlink()

    return Response(result)

def home(request):
    return render(request, 'index.html')