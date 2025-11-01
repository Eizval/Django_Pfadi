# forms.py
from django import forms
from .models import Item, Stock, Borrow, Sold


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
        widgets = {
            'returned_at': forms.DateInput(attrs={'type': 'date'})
        }

class SoldForm(forms.ModelForm):
    class Meta:
        model = Sold
        fields = ['item', 'email', 'quantity', 'sold_at', 'notes']
        widgets = {
            'sold_at': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }