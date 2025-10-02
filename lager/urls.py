from django.urls import path
from . import views

urlpatterns = [
    path('lager_edit/', views.lager_edit_view, name='lager_edit'),
    path('lager_list/', views.lager_list_view, name='lager_list'),
]