from django.urls import path
from . import views

urlpatterns = [
    path('admin_register/', views.admin_register, name='admin_register'),
    path('admin_otp/', views.admin_otp, name='admin_otp'),
    path('admin_login/', views.admin_login, name='admin_login'),
]
