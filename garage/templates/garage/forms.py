from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        # We include all fields except 'added_on' since that is automatic
        fields = ['make', 'model_name', 'vehicle_type', 'year', 'engine_specs', 'horsepower', 'description']
        
        # Adding some Bootstrap CSS classes to make the form look good
        widgets = {
            'make': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Subaru'}),
            'model_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., WRX STI'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-select'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'engine_specs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 2.5L Turbocharged Boxer'}),
            'horsepower': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        