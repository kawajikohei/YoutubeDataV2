import requests
from PIL import Image
from io import BytesIO

def image_ld(image):
    profile_image_url = image
    response = requests.get(profile_image_url)
    response = BytesIO(response.content)
    img = Image.open(response)
    img = img.save("test","JPEG")
    return img
