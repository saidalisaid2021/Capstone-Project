from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from .models import MenuItem,Menu,Booking
from django.contrib.auth.models import User
from .serializers import MenuItemSerializer, MenuSerializer, BookingSerializer, UserSerializer



# Create your views here.
from django.http import HttpResponse

def sayHello(request):
 return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class MenuView(APIView):
    def get(self,request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class =BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
        
class MenuItemsView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]
   
   
@api_view()
@permission_classes([permissions.IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})