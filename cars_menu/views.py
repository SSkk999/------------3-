from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from cars_menu.models import Car
from django.views.decorators.csrf import csrf_exempt
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