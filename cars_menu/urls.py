from django.urls import path

from cars_menu import views

urlpatterns = [
    path('', views.index ,name='car_list'),
    path('cars/<int:id>/', views.car , name='car_detail'),
    path('delete/<int:id>/', views.delete_car, name='delete_car')
]