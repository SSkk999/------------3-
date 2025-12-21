from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from cars_menu.models import Car
from django.views.decorators.csrf import csrf_exempt
from cars_menu.forms.car import CarsForm
def index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def car(request, id):
     car = Car.objects.get(pk =id)
     return render(request, 'cars/car.html', {'car': car})

@csrf_exempt
def delete_car(request, id):
     car = Car.objects.get(pk = id)
     car.delete()
     return redirect(request.META.get('HTTP_REFERER', '/'))

def adminpanel(request):
    cars = Car.objects.all()
    return render(request, 'cars/adminpanel.html', {'cars': cars})

def create(request):
     if request.method == 'POST':
        cars_form = CarsForm(request.POST)
        if cars_form.is_valid():
            cars_form.save()
            return redirect('adminpanel')
     cars_form = CarsForm()
     return render(request, 'cars/create.html', {'form': cars_form})
def update_car(request, id):
     car = get_object_or_404(Car,pk=id)
     if request.method == 'POST':
        cars_form = CarsForm(request.POST, instance=car)
        if cars_form.is_valid():
            cars_form.save()
            return redirect('adminpanel')
     cars_form = CarsForm(instance=car)
     return render(request, 'cars/update.html', {'form': cars_form})