from django.forms import ModelForm      #instead of writing forms manually
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'  #creates a form based on Room attributes
