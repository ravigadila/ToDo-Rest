from rest_framework import generics

from todo.models import List, Item
from api.serializers import ListSerializer, ItemSerializer


class CreateList(generics.CreateAPIView):
    """
    Acceptes: POST
    201: created
    """
    serializer_class = ListSerializer


class EditList(generics.RetrieveUpdateDestroyAPIView):
    """
    Responses
    accepts, GET, PUT, DELETE
    200: Edit, delete
    204: deleted
    """
    queryset = List.objects.all()
    serializer_class = ListSerializer


class AllLists(generics.ListAPIView):
    """
    AllLists
    """
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CreateItem(generics.CreateAPIView):
    """
    Acceptes: POST
    201: created
    """
    serializer_class = ItemSerializer


class EditItem(generics.RetrieveUpdateDestroyAPIView):
    """
    Responses
    accepts, GET, PUT, DELETE
    200: Edit, delete
    204: deleted
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
