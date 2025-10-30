from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Item, Stock, Borrow, Pending, Sold
from .decorators import role_or_superuser_required

@login_required
def lager_edit_view(request):
    return render(request, "lager/lager_edit.html", {})

@login_required
def lager_list_view(request):
    """Display tables based on user permissions"""
    tables = []

    # Immer sichtbar
    tables.append({"name": "Artikel", "model": "item", "count": Item.objects.count()})
    tables.append({"name": "Lagerbestand", "model": "stock", "count": Stock.objects.count()})

    # Sichtbar nur für Admin, Superuser oder bestimmte Rollen
    allowed_roles = [1]  # hier kannst du weitere Rollen-IDs hinzufügen
    if request.user.is_superuser or request.user.is_staff or request.user.role_id in allowed_roles:
        tables.append({"name": "Ausleihe", "model": "borrow", "count": Borrow.objects.count()})
        tables.append({"name": "Gekauft", "model": "sold", "count": Sold.objects.count()})
        tables.append({"name": "Bestellt", "model": "pending", "count": Pending.objects.count()})

    return render(request, "lager/lager_list.html", {"tables": tables})


@login_required
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
@login_required
def item_list(request):
    items = Item.objects.all()
    return render(request, "lager/item.html", {"objects": items})

# Stock list page
@login_required
def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, "lager/stock.html", {"objects": stocks})

# Borrow list page
@login_required
@role_or_superuser_required(1)
def borrow_list(request):
    borrows = Borrow.objects.all()
    return render(request, "lager/borrow.html", {"objects": borrows})

@login_required
@role_or_superuser_required(1)
def pending_list(request):
    pending_items = Pending.objects.all()
    return render(request, "lager/pending.html", {"objects": pending_items})

@login_required
@role_or_superuser_required(1)
def sold_list(request):
    sold_items = Sold.objects.all()
    return render(request, "lager/sold.html", {"objects": sold_items})