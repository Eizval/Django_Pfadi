from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Category, Item, Stock, Borrow

@login_required
def lager_edit_view(request):
    return render(request, "lager/lager_edit.html", {})

@login_required
def lager_list_view(request):
    """Display an overview of all tables (ER diagram style)"""
    tables = [
        {"name": "Kategorie", "model": "category", "count": Category.objects.count()},
        {"name": "Artikel", "model": "item", "count": Item.objects.count()},
        {"name": "Lagerbestand", "model": "stock", "count": Stock.objects.count()},
        {"name": "Ausleihe", "model": "borrow", "count": Borrow.objects.count()},
    ]
    return render(request, "lager/lager_list.html", {"tables": tables})

def table_detail(request, table_name):
    """Display items of a specific table"""
    if table_name == "category":
        objects = Category.objects.all()
        fields = [f.verbose_name for f in Category._meta.fields]
    elif table_name == "item":
        objects = Item.objects.all()
        fields = [f.verbose_name for f in Item._meta.fields]
    elif table_name == "stock":
        objects = Stock.objects.all()
        fields = [f.verbose_name for f in Stock._meta.fields]
    elif table_name == "borrow":
        objects = Borrow.objects.all()
        fields = [f.verbose_name for f in Borrow._meta.fields]
    else:
        objects = []
        fields = []

    return render(request, f"lager/{table_name}.html", {"objects": objects, "fields": fields})

# Category list page
def category_list(request):
    categories = Category.objects.all()
    return render(request, "lager/category.html", {"objects": categories})

# Item list page
def item_list(request):
    items = Item.objects.all()
    return render(request, "lager/item.html", {"objects": items})

# Stock list page
def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, "lager/stock.html", {"objects": stocks})

# Borrow list page
def borrow_list(request):
    borrows = Borrow.objects.all()
    return render(request, "lager/borrow.html", {"objects": borrows})