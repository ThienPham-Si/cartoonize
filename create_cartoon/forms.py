from django import forms
from .models import CartoonModel

class CartoonForm(forms.ModelForm):
    class Meta:
        model = CartoonModel
        fields = ['img']
