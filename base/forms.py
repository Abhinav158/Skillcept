from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):

    # This creates the form based on the metadata given below
    class Meta:
        model = Room
        fields = '__all__'
        # The host should automatically become the user who is creating the room
        exclude = ['host', 'participants']
        