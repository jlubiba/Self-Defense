from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, throttle_classes, api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the welcoming page!")

class category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
            user = self.request.user
            if user.groups.filter(name='General Manager' or 'Tutorial Manager'):
                serialized_items = CategorySerializer(self.queryset)
                return Response(serialized_items.data, status=status.HTTP_200_OK)
        
        return [permission() for permission in permission_classes]

# class moves(viewsets.ModelViewSet):
#     queryset = Moves.objects.all()
    