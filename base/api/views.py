# We want to respond with some JSON data when someone goes to our URL 

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RoomSerializer
from base.models import Room

# Users can only get data so allow only GET requests 
@api_view(['GET'])

# This view will show us all the routes in our API 
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routes)


@api_view(['GET'])

# Allow users to gain access to all our rooms 
def getRooms(request):
    rooms = Room.objects.all()

    # Many is true since we are going to serialize many objects
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])

# Give access to a specific room using room id 
def getRoom(request, pk):
    room = Room.objects.get(id=pk)

    # Return a single object 
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)