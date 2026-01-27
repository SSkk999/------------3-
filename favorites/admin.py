from django.contrib import admin

from cars_menu.models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price','category']
    search_fields = ['name', 'category','description']
    list_filter = ['category']

admin.site.register(Car, CarAdmin)

