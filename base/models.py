# This is where we create our database tables 

# The classes we create represent a database table - every attribute in the class is a column 
# Every time we make an instance of the class, it is creating a new row in the table 

from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)

    # Create a string representation of this room
    def __str__(self):
        return self.name



# Setting null to true means that the field can be blank, default is false
# Blank is for the form submit purposes 
# Auto_now creates a timestamp everytime we save the item wheras auto_now_add saves only the first time it is saved
class Room(models.Model):
    host = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # A topic can have multiple rooms but one room can contain only 1 topic 
    # If a topic is deleted, we can set the room to NULL 
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # String Representation
    def __str__(self):
        return self.name


class Message(models.Model):
    # A user can send multiple messages but a message can be sent only by one user 
    # If a user is deleted, we want to delete all his messages
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # If room is deleted, delete all the messages in that room 
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # String Representation
    def __str__(self):
        return self.body[0:50]



