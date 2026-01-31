from django.conf import settings
from django.urls import path
    
from cars_menu import views

from django.conf.urls.static import static

urlpatterns = [
    path('', views.index ,name='car_list'),
    path('cars/<int:id>/', views.car , name='car_detail'),
    path('delete/<int:id>/', views.delete_car, name='delete_car'),
    path('adminpanel', views.adminpanel ,name='adminpanel'),
    path('cars/create/', views.create ,name='create'),
    path('cars/update/<int:id>/', views.update_car, name='update'),
    path('favorites/', views.index, {'filter_by_favorites': True}, name='favorites'),
]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
