from django.shortcuts import render, redirect
from .models import Vehicle, PurchaseOrder
from .forms import VehicleForm  # You will create this form in the next step


def index(request):
    return render(request,'vehicle/base.html')

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle/vehicle.html', {'vehicles': vehicles})

def add_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicle/add_vehicle.html', {'form': form})

