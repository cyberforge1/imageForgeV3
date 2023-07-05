'''Defines URL patterns for image_generation.'''

from django.urls import path


# Additions to fetch an image
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'image_generation'

urlpatterns = [
    # User History
    path('user_history/', views.user_history, name='user_history'),
    # A View of the Generated Images.
    path('generated_images/', views.generated_image_view, name='generated_images'),
    # Other URL patterns...
    # Public Gallery
    path('gallery/', views.gallery, name='gallery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)