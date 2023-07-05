import os
import requests
from create_image import generate_image_url, PROMPT
from dotenv import load_dotenv

load_dotenv()

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "media")

def save_image_from_url(url, prompt):
    response = requests.get(url)
    image_path = os.path.join(MEDIA_ROOT, f"image{prompt}.jpg")
    
    with open(image_path, "wb") as f:
        f.write(response.content)
    
    print(f"Image saved as {image_path}")

# Main execution
image_url = generate_image_url()
if image_url:
    save_image_from_url(image_url, PROMPT)



