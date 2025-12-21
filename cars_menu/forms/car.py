from django import forms
from cars_menu.models import Car

class CarsForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product name'}),
            'image': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Image URL'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Price'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }