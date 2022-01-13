from pyexpat import model
from turtle import mode
from django.forms import ModelForm
from .models import Room
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
