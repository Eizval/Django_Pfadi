from django.urls import path
from . import views

urlpatterns = [
    path("", views.profiles_list, name="profiles"),
    path("add/", views.profile_add, name="profile_add"),
    path("<int:pk>/edit/", views.profile_edit, name="profile_edit"),
    path("<int:pk>/delete/", views.profile_delete, name="profile_delete"),
]
