from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# github.com/m4xy07
# Rename index to home to match URL pattern name if needed
def index(request):
    return render(request, 'index.html', {})

# Menu Function
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', main_data)

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})

def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')

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
