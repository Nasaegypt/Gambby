import cities_light.models
from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        exclude = ['slug', 'owner']

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        # for select city dependent to service region
        # self.fields['service_city'].queryset = cities_light.models.City.objects.none()
        self.fields['image'].required = False
