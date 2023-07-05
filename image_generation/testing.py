import os


MEDIA_ROOT1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "media")

print(MEDIA_ROOT1)


MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "media")

print(MEDIA_ROOT)