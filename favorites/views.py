from django.shortcuts import redirect, render
from favorites.favorites import add_car_to_favorites, remove_car_from_favorites

def add_car(request, car_id, return_url):
    add_car_to_favorites(request, car_id)
    return redirect(return_url)

def remove_car(request, car_id, return_url):
    remove_car_from_favorites(request, car_id)
    return redirect(return_url)