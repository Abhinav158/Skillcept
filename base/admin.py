from django.contrib import admin

# This is where we register all our models to be able to access it in Django Admin panel 

from .models import Room, Topic, Message, User 

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

