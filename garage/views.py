from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Vehicle
from .forms import VehicleForm

def vehicle_list(request):
    vehicles = Vehicle.objects.all().order_by('-added_on')
    
    # --- SEARCH LOGIC ---
    search_query = request.GET.get('q')
    if search_query:
        vehicles = vehicles.filter(
            Q(make__icontains=search_query) | 
            Q(model_name__icontains=search_query) |
            Q(engine_specs__icontains=search_query)
        )

    # --- PAGINATION LOGIC (9 vehicles per page) ---
    paginator = Paginator(vehicles, 9) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj': page_obj, 'search_query': search_query}
    return render(request, 'garage/vehicle_list.html', context)

def add_vehicle(request):
    if request.method == 'POST':
        # request.FILES is required to grab the uploaded image
        form = VehicleForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    
    context = {'form': form}
    return render(request, 'garage/add_vehicle.html', context)

def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        # request.FILES added here as well so you can change the image later
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
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