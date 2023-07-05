from django.contrib import admin

from .models import RandomPrompt, GeneratedImage

admin.site.register(RandomPrompt)

admin.site.register(GeneratedImage)