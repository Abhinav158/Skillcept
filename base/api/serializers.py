# Classes that take a model and convert it into JSON object to return it 

from rest_framework.serializers import ModelSerializer
from base.models import Room 

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'