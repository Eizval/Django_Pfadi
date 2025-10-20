from django.urls import path
from . import views

urlpatterns = [
    path('lager_edit/', views.lager_edit_view, name='lager_edit'),
    path('lager_list/', views.lager_list_view, name='lager_list'),
    path("table/<str:table_name>/", views.table_detail, name="table_detail"),
    path("categories/", views.category_list, name="category_list"),
    path("items/", views.item_list, name="item_list"),
    path("stocks/", views.stock_list, name="stock_list"),
    path("borrows/", views.borrow_list, name="borrow_list"),
]
