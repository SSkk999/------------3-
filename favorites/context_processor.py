from favorites.favorites import get_count_of_favorite_car

def favorite_list_count(request):
    return { 'favorite_count': get_count_of_favorite_car(request) }