from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def lager_edit_view(request):
    return render(request, "lager/lager_edit.html", {})

@login_required
def lager_list_view(request):
    return render(request, "lager/lager_list.html", {})