from google.cloud import vision
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\shiva\Desktop\PriceAPI\product_scraper\scraper\gen-lang-client-0654264515-111de3b90c98.json"

def detect_logo_and_objects(image_path):
    # Initialize the Vision API client
    client = vision.ImageAnnotatorClient()

    # Load the image into memory
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # Detect logos
    logo_response = client.logo_detection(image=image)
    logos = logo_response.logo_annotations

    # Detect objects
    object_response = client.object_localization(image=image)
    objects = object_response.localized_object_annotations

    # Identify the logo with the highest confidence
    top_logo = max(logos, key=lambda l: l.score, default=None)

    # Identify the object with the highest confidence
    top_object = max(objects, key=lambda o: o.score, default=None)

    result=[]
    # Display the highest confidence logo
    if top_logo:
        result.append(top_logo.description)
    else:
        print("No logos detected.")

    # Display the highest confidence object
    if top_object:
        result.append(top_object.name)
    else:
        print("No objects detected.")

    # Handle errors
    if logo_response.error.message:
        raise Exception(f"Logo Detection Error: {logo_response.error.message}")
    if object_response.error.message:
        raise Exception(f"Object Detection Error: {object_response.error.message}")
    return result

# Example Usage: Replace 'path_to_your_image.jpg' with the path to your image file
# print(detect_logo_and_objects('img2.jpeg'))
