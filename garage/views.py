from django.shortcuts import render, redirect, get_object_or_404
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

def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        # 'instance=vehicle' tells Django to update the existing record instead of creating a new one
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'garage/add_vehicle.html', {'form': form, 'edit_mode': True})

def delete_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'garage/delete_confirm.html', {'vehicle': vehicle})