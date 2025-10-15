from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('approve/', views.approve_view, name='approve'),
    path('approve/<int:user_id>/', views.approve_user, name='approve_user'),
]
