from django.shortcuts import render, redirect
from .models import Room 
from .forms import RoomForm
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


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        # print(request.POST) - works! - data from form submitted shown 
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)