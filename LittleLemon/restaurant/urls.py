from django.contrib import admin 
from django.urls import path , include
from rest_framework.authtoken.views import obtain_auth_token

from . import views 
  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    # path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', views.BookingViewSet.as_view()),
    path('booking/<int:pk>', views.SingleBookingView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]