from django.urls import path

from favorites import views

urlpatterns = [
    # path('', views.index, name='favorites_index'),
    path('add/<int:car_id>/<str:return_url>/', views.add_car, name='add_fav_car'),
    path('remove/<int:car_id>/<str:return_url>/', views.remove_car, name='remove_fav_car'),
    path('list/', views.car_favorites_cat, name='favorites_list'),
]