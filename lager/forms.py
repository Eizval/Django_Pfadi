# forms.py
from django import forms
from .models import Item, Stock

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'sku', 'unit', 'quantity', 'size', 'description']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['quantity', 'location', 'item']