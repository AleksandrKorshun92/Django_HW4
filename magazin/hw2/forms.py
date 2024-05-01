from datetime import datetime

from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form_control",
                                                                         "placeholder": "напишите название продукта"}))
    describe = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField()

class ImageForm(forms.Form):
    image = forms.ImageField()
