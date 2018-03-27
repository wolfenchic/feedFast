from django import forms
from .models import Restaurant, Menu, Menu_item

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('vendor', 'name', 'description', 'city', 'image', 'tag')
        
class createMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name',)