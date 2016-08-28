from rest_framework import generics

from todo.models import List, Item
from api.serializers import ListSerializer, ItemSerializer


class CreateList(generics.CreateAPIView):
    serializer_class = ListSerializer
