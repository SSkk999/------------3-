from django.shortcuts import redirect, render
from favorites.favorites import add_car_to_favorites, remove_car_from_favorites,get_favorite_car,get_count_of_favorite_car
from cars_menu.models import Car

def add_car(request, car_id, return_url):
    add_car_to_favorites(request, car_id)
    return redirect(return_url)

def remove_car(request, car_id, return_url):
    remove_car_from_favorites(request, car_id)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def car_favorites_cat(request):
    carsf = get_favorite_car(request)
    cars = Car.objects.filter(id__in=carsf)
    return render(request, 'favorites_list.html', {
        'cars': cars, 
        "fav_count": get_count_of_favorite_car(request),
        "fav_ids": get_favorite_car(request),
     }
     )

