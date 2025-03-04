from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# github.com/m4xy07
def index(request):
    context = {}
    return render(request, 'index.html', context)

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
