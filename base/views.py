from django.shortcuts import render

# This request tells us what kind of data is going to be passed in to the backend by the user 
def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html')