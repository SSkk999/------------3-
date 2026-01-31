from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars_menu.urls')),
    path('favorites/', include('favorites.urls')),

]