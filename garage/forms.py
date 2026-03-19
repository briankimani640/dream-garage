from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model_name', 'vehicle_type', 'year', 'engine_specs', 'horsepower', 'description', 'image']
        
        widgets = {
            'make': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Subaru'}),
            'model_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., WRX STI'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-select'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'engine_specs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 2.5L Turbocharged Boxer'}),
            'horsepower': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        