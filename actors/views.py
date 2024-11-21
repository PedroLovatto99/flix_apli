from rest_framework import generics
from .models import *
from actors.serializers import *
from rest_framework.permissions import IsAuthenticated
from app.permissions import *

class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer