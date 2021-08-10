from .serializers import RoomSerializer, CreateRoomSerializer
from rest_framework import generics, status
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class RoomView(generics.ListAPIView):
  queryset = Room.objects.all()
  
  serializer_class = RoomSerializer

class CreateRoomView(APIView):
  serializer_class = CreateRoomSerializer
  def post(self, request, format=None):
    if not self.request.session.exists(self.request.session.session_key):
      print('-------------------------------------------------------')
      self.request.session.create()
      print(request.data)
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      guest_can_pause = serializer.data.get('guest_can_pause')
      votes_to_skip = serializer.data.get('votes_to_skip')
      host = self.request.session.session_key
      queryset = Room.objects.filter(host=host)
      if queryset.exists(): #if the host already has a room
        room = queryset[0]  # set room var to the same room the host already had
        room.guest_can_pause = guest_can_pause
        room.votes_to_skip = votes_to_skip
        room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
        return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
      else: # the host doesn't have a room 
        room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
        room.save()
        return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
    return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)