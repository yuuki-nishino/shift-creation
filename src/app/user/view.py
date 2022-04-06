from rest_framework import generics
from .models import Store,User,Shift
from .serializers import StoreSerializer, UserSerializer,ShiftSerializer

class StoreList(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ShiftList(generics.ListAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
