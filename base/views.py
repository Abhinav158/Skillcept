from django.shortcuts import render
from .models import Room 

# The request parameter tells us what kind of data is going to be passed in to the backend by the user 

def home(request):

    # Give us all rooms in the database 
    rooms = Room.objects.all()

    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)    
    context = {'room': room}
    return render(request, 'base/room.html', context)