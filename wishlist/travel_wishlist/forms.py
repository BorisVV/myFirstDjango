
from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
    """docstring for form namen and visited locations."""
    class Meta:
        model = Place
        fields = ('name', 'visited')
