from django.urls import path
from . import views

urlpatterns = [
    path('lager_edit/', views.lager_edit_view, name='lager_edit'),
    path('lager_list/', views.lager_list_view, name='lager_list'),
    path("table/<str:table_name>/", views.table_detail, name="table_detail"),
    path("items/", views.item_list, name="item_list"),
    path('items/new/', views.item_create, name='item_create'),
    path('items/<int:pk>/edit/', views.item_edit, name='item_edit'),
    path('items/<int:pk>/delete/', views.item_delete, name='item_delete'),
    path("stocks/", views.stock_list, name="stock_list"),
    path("stocks/new/", views.stock_create, name='stock_create'),
    path('stocks/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stocks/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path("borrows/", views.borrow_list, name="borrow_list"),
    path("borrows/new/", views.borrow_create, name="borrow_create"),
    path("borrows/<int:pk>/edit/", views.borrow_edit, name="borrow_edit"),
    path("borrows/<int:pk>/delete/", views.borrow_delete, name="borrow_delete"),
    path("pending/", views.pending_list, name="pending_list"),
    path("pending/new/", views.pending_create, name="pending_create"),
    path("pending/<int:pk>/edit/", views.pending_edit, name="pending_edit"),
    path("pending/<int:pk>/delete/", views.pending_delete, name="pending_delete"),
    path("sold/", views.sold_list, name="sold_list"),
    path("sold/new/", views.sold_create, name="sold_create"),
    path("sold/<int:pk>/edit/", views.sold_edit, name="sold_edit"),
    path("sold/<int:pk>/delete/", views.sold_delete, name="sold_delete"),
]
