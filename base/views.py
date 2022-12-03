from django.shortcuts import render

# The request parameter tells us what kind of data is going to be passed in to the backend by the user 

rooms = [
    {'id': 1, 'name': 'Learn ReactJS'},
    {'id': 2, 'name': 'NodeJS Crash Course'},
    {'id': 3, 'name': 'Django Developers'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    
    context = {'room': room}
    return render(request, 'base/room.html', context)