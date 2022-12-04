from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

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
        fields = ['username', 'email']