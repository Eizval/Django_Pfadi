from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Item, Stock, Borrow, Pending, Sold

@login_required
def lager_edit_view(request):
    return render(request, "lager/lager_edit.html", {})

@login_required
def lager_list_view(request):
    """Display an overview of all tables (ER diagram style)"""
    tables = [
        {"name": "Artikel", "model": "item", "count": Item.objects.count()},
        {"name": "Lagerbestand", "model": "stock", "count": Stock.objects.count()},
        {"name": "Ausleihe", "model": "borrow", "count": Borrow.objects.count()},
        {"name": "Gekauft", "model": "sold", "count": Sold.objects.count()},
        {"name": "Bestellt", "model": "pending", "count": Pending.objects.count()},
    ]
    return render(request, "lager/lager_list.html", {"tables": tables})

def table_detail(request, table_name):
    """Display items of a specific table"""
    if table_name == "item":
        objects = Item.objects.all()
        fields = [f.verbose_name for f in Item._meta.fields]
    elif table_name == "stock":
        objects = Stock.objects.all()
        fields = [f.verbose_name for f in Stock._meta.fields]
    elif table_name == "borrow":
        objects = Borrow.objects.all()
        fields = [f.verbose_name for f in Borrow._meta.fields]
    elif table_name == "sold":
        objects = Sold.objects.all()
        fields = [f.verbose_name for f in Sold._meta.fields]
    elif table_name == "pending":
        objects = Pending.objects.all()
        fields = [f.verbose_name for f in Pending._meta.fields]
    else:
        objects = []
        fields = []

    return render(request, f"lager/{table_name}.html", {"objects": objects, "fields": fields})

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

def pending_list(request):
    pending_items = Pending.objects.all()
    return render(request, "lager/pending.html", {"objects": pending_items})

def sold_list(request):
    sold_items = Sold.objects.all()
    return render(request, "lager/sold.html", {"objects": sold_items})