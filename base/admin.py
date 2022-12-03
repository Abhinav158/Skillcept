from django.contrib import admin

# This is where we register all our models to be able to access it in Django Admin panel 

from .models import Room

admin.site.register(Room)

