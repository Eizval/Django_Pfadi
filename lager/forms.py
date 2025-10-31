# forms.py
from django import forms
from .models import Item, Stock, Borrow


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'sku', 'unit', 'quantity', 'size', 'description']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['quantity', 'location', 'item']

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['quantity', 'returned_at', 'status', 'user', 'item']