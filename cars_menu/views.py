from django.shortcuts import render

def index(request):
    return render(request, 'cars/index.html')

cars = [
    {
        'id': 1,
        'name': 'BMW',
        'description': 'Sport sedan',
        'image': 'https://images.unsplash.com/photo-1502877338535-766e1452684a'
    },
    {
        'id': 2,
        'name': 'Audi',
        'description': 'Quattro AWD',
        'image': 'https://images.unsplash.com/photo-1549924231-f129b911e442'
    },
    {
        'id': 3,
        'name': 'Mercedes',
        'description': 'Luxury class',
        'image': 'https://images.unsplash.com/photo-1511919884226-fd3cad34687c'
    },
]
def car(request, id):
     car = next((c for c in cars if c['id'] == id), None)
     return render(request, 'cars/car.html', {'car': car})