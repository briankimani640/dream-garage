from django.urls import path
from . import views

urlpatterns = [
    # This makes the vehicle list show up right on the homepage
    path('', views.vehicle_list, name='vehicle_list'), 
    path('add/', views.add_vehicle, name='add_vehicle'),
    
]