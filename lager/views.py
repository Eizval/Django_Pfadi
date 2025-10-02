from django.shortcuts import render

# Create your views here.
def lager_edit_view(request):
    return render(request, "lager/lager_edit.html", {})

def lager_list_view(request):
    return render(request, "lager/lager_list.html", {})