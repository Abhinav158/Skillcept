from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1', 'password2']

class RoomForm(ModelForm):

    # This creates the form based on the metadata given below
    class Meta:
        model = Room
        fields = '__all__'
        # The host should automatically become the user who is creating the room
        exclude = ['host', 'participants']
        

class UserForm(ModelForm):

    class Meta:
        model = User 
        fields = ['avatar','name','username', 'email','bio']