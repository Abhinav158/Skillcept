from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):

    # This creates the form based on the metadata given below
    class Meta:
        model = Room
        fields = '__all__'
        