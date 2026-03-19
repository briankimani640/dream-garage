from django.shortcuts import render, redirect
from .models import Vehicle
from .forms import VehicleForm

def vehicle_list(request):
    vehicles = Vehicle.objects.all().order_by('-added_on')
    context = {'vehicles': vehicles}
    return render(request, 'garage/vehicle_list.html', context)

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save() # Saves the new vehicle to the SQLite database
            return redirect('vehicle_list') # Sends you back to the homepage
    else:
        form = VehicleForm() # Creates an empty form if just visiting the page
    
    context = {'form': form}
    return render(request, 'garage/add_vehicle.html', context)