from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from cars_menu.models import Car
from django.views.decorators.csrf import csrf_exempt
from cars_menu.forms.car import CarsForm
from django.contrib import messages
from favorites.favorites import get_count_of_favorite_car, get_favorite_car
def index(request, filter_by_favorites=False):
    cars = Car.objects.all()
    category = request.GET.get('category')
    selected_category = category
    if category:
        cars = cars.filter(category=category)
    else:
        cars = Car.objects.all()
    if filter_by_favorites:
        fav_ids = get_favorite_car(request)
        cars = cars.filter(id__in=fav_ids)

    filter_text = request.GET.get("filter_text", "")

    if filter_text:
        cars = cars.filter(name__icontains=filter_text)
    
    return render(request, 'cars/index.html', {
        'cars': cars, 
        "fav_count": get_count_of_favorite_car(request),
        "fav_ids": get_favorite_car(request),
        'selected_category': category
     }
     )
def car(request, id):
     car = Car.objects.get(pk =id)
     return render(request, 'cars/car.html', {'car': car})

@csrf_exempt
def delete_car(request, id):
     car = Car.objects.get(pk = id)
     car.delete()
     messages.success(request, f"Cars has been delete  successfully!","red")
     return redirect(request.META.get('HTTP_REFERER', '/'))

def adminpanel(request):
    cars = Car.objects.all()
    return render(request, 'cars/adminpanel.html', {'cars': cars})

def create(request):
     if request.method == 'POST':
        cars_form = CarsForm(request.POST , request.FILES)
        if cars_form.is_valid():
            cars_form.save()
            messages.success(request, f"Cars has been created  successfully!","green")
            return redirect('adminpanel')
     cars_form = CarsForm()
     return render(request, 'cars/create.html', {'form': cars_form})
def update_car(request, id):
     car = get_object_or_404(Car,pk=id)
     if request.method == 'POST':
        cars_form = CarsForm(request.POST, request.FILES,instance=car)
        if cars_form.is_valid():
            cars_form.save()
            messages.success(request, f"Cars has been updated successfully!","green")
            return redirect('adminpanel')
     cars_form = CarsForm(instance=car)
     return render(request, 'cars/update.html', {'form': cars_form})