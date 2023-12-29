from django.shortcuts import render
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]