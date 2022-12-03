# This is where we create our database tables 

# The classes we create represent a database table - every attribute in the class is a column 
# Every time we make an instance of the class, it is creating a new row in the table 

from django.db import models

# Setting null to true means that the field can be blank, default is false
# Blank is for the form submit purposes 
# Auto_now creates a timestamp everytime we save the item wheras auto_now_add saves only the first time it is saved
class Room(models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # Create a string representation of this room
    def __str__(self):
        return self.name


