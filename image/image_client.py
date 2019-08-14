import hashlib
import requests
from io import BytesIO

def get(url):
    response = requests.get(url)
    return BytesIO(response.content)

def hexdigest(image_binary):
    """ accepts a BytesIO representation of an image (e.g., from `image_client.get()`) """
    return hashlib.md5(image_binary.getvalue()).hexdigest()
