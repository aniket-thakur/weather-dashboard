from django import forms
from dashboard.models import City
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('city_name',)
        widgets = {
            'city_name': forms.TextInput(attrs={'class': 'form-control my-4 w-75 mx-auto','placeholder':'city name:'})

        }
