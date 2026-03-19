from django.urls import path
from . import views

urlpatterns = [
    # This makes the vehicle list show up right on the homepage
    path('', views.vehicle_list, name='vehicle_list'), 
    path('add/', views.add_vehicle, name='add_vehicle'),
    path('edit/<int:pk>/', views.edit_vehicle, name='edit_vehicle'),
    path('delete/<int:pk>/', views.delete_vehicle, name='delete_vehicle'),

]