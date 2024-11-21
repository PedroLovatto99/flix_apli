from rest_framework import generics
from .models import *
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import *

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass)


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass)





