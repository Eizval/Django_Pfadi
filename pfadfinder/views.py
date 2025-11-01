from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")


def hub_view(request):
    return render(request, "hub.html")
