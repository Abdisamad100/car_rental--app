from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    path('rent/', views.rent_car, name='rent_car'),
    path('return/', views.return_car, name='return_car'),
    path('login/', views.login_view, name='login'),  # Update here
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('car_log_history/', views.car_log_history, name='car_log_history'),  # New URL for history
    path('car-log-history/', views.car_log_history, name='car_log_history'),
    path('car-log-create/', views.car_log_create, name='car_log_create'),
    path('custom_admin/', views.custom_admin, name='custom_admin'),
    path('car-log-edit/<int:pk>/', views.car_log_edit, name='car_log_edit'),
    path('car-log-delete/<int:pk>/', views.car_log_delete, name='car_log_delete'),  # New URL for editing
]
