from django import forms
from .models import CarRental, CarReturn
from django import forms
from .models import CarRental

class RentCarForm(forms.ModelForm):
    class Meta:
        model = CarRental
        fields = ['car_model', 'car_registration', 'car_journey', 'car_milege', 'fuel_used']

class CarRentalForm(forms.ModelForm):
    class Meta:
        model = CarRental
        fields = ['car_model', 'car_registration', 'car_journey', 'car_milege', 'fuel_used']
        widgets = {
            'car_model': forms.TextInput(attrs={'class': 'form-control'}),
            'car_registration': forms.TextInput(attrs={'class': 'form-control'}),
            'car_journey': forms.TextInput(attrs={'class': 'form-control'}),
            'car_milege': forms.TextInput(attrs={'class': 'form-control'}),
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control'}),
            'fuel_used': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CarReturnForm(forms.ModelForm):
    class Meta:
        model = CarReturn
        fields = ['car_picture', 'condition', 'issues']
        widgets = {
            'car_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'condition': forms.Textarea(attrs={'class': 'form-control'}),
            'issues': forms.Textarea(attrs={'class': 'form-control'}),
        }
