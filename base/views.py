from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

from .models import Room, Topic, Message
from .forms import RoomForm, UserForm
# The request parameter tells us what kind of data is going to be passed in to the backend by the user 

def loginPage(request):

    page = 'login'

    # If a user has already logged in, he should not be able to visit the login page
    # Send him back to the Home page
    if request.user.is_authenticated:
        return redirect ('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        # Make sure that the user exists
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        # Gives an error or given a user object that matches the credentials 
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Go ahead and login this user - add the session in the db and user is logged in
            login(request, user)
            return redirect ('home')
        else:
            messages.error(request, 'Username OR Password does not exist')

        
    context = {'page': page}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Form Validation - correct everything the user has entered before submitting
            user.username = user.username.lower()
            user.save()
            # Login the user who just registered
            login(request, user)
            return redirect('home')
        # Error occured 
        else: 
            messages.error(request, 'An Error occurred during Registration')

    context = {'form': form}
    return render(request, 'base/login.html', context)

def home(request):

    # Search functionality implementation
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))

    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk) 
    # Get the set of messages related to one particular room 
    # Display the comment list with the most recent message on top
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method == 'POST':
        # Go ahead and create a message  
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        # Add the current user to the many to many field 
        room.participants.add(request.user)
        return redirect('room',pk=room.id)  
    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/room.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)

# We want to remove the Create Room option if the user has not logged in
# Redirect user to Login page incase he has not yet logged in
# Apply the same to Room Update and Delete functionality 
@login_required(login_url='login')
def createRoom(request):
    
    form = RoomForm()

    # Grab all the topics to pass it into the template 
    topics = Topic.objects.all()
    if request.method == 'POST':
        # print(request.POST) - works! - data from form submitted shown 
        # form = RoomForm(request.POST)
        topic_name = request.POST.get('topic')

        # If a new topic has been created in a room, add this to the topics database 
        topic, create = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
             topic=topic,
             name=request.POST.get('name'),
             description=request.POST.get('description'),
        )
       
        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) 
    # Grab all the topics to pass it into the template 
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')

        # If a new topic has been created in a room, add this to the topics database 
        topic, create = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk) 

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')
        
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {'obj': room}
    return render(request, 'base/delete.html', context)

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk) 

    if request.user != message.user:
        return HttpResponse('You cannot Delete this!')
        
    if request.method == 'POST':
        message.delete()
        return redirect('home')

    context = {'obj': message}
    return render(request, 'base/delete.html', context)

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)


    context = {'form': form}
    return render(request, 'base/update-user.html', context)

