from django.db import models

class RandomPrompt(models.Model):
    '''A random prompt generated for the user'''
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def get_text(self):
        return self.text_field
    
    def get_datetime(self):
        return self.datetime_field

class GeneratedImage(models.Model):
    text_field = models.TextField()
    datetime_field = models.DateTimeField(auto_now_add=True)
    image_field = models.ImageField(upload_to='images/')
    
    def save(self, *args, **kwargs):
        # Generate and set the image URL before saving the model
        if not self.pk and not self.image_field:
            self.image_field = generate_image_url(self.text_field)
        super().save(*args, **kwargs)

    def get_text(self):
        return self.text_field

    def get_datetime(self):
        return self.datetime_field

    def get_image_url(self):
        if self.image_field:
            return self.image_field.url
        return None