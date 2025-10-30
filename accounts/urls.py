from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('approve/', views.approve_view, name='approve'),
    path('approve/<int:user_id>/', views.approve_user, name='approve_user'),
    path('logout/', views.logout_view, name='logout'),
    path('all_users/', views.all_users_view, name='all_users'),
    path('role/', views.role_view, name='role'),
    path('all_users/<int:user_id>/', views.add_role_view, name='add_role'),
    path('create_role/', views.create_role_view, name='create_role'),
    path('role/<int:role_id>', views.delete_role_view, name='delete_role'),
]
