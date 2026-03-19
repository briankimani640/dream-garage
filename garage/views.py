from django.shortcuts import render
from .models import Vehicle

def vehicle_list(request):
    # To fetch all vehicles from the database, ordered by the newest added first
    vehicles = Vehicle.objects.all().order_by('-added_on')
    
    # Pass the data to the template using a context dictionary
    context = {
        'vehicles': vehicles
    }
    return render(request, 'garage/vehicle_list.html', context)