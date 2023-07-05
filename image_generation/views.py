from django.shortcuts import render

from .models import RandomPrompt, GeneratedImage

def user_history(request):
    '''Show all user history entries.'''
    user_history = RandomPrompt.objects.order_by('date_added')
    context = {'user_history': user_history}
    return render(request, 'image_generation/user_history.html', context)


def gallery(request):
    generated_images = GeneratedImage.objects.all()
    context = {
        'generated_images': generated_images,
    }
    return render(request, 'image_generation/gallery.html', context)


def generated_image_view(request):
    # Retrieve all GeneratedImage objects
    generated_images = GeneratedImage.objects.all()
    context = {
        'generated_images': generated_images
    }
    return render(request, 'image_generation/generated_images.html', context)