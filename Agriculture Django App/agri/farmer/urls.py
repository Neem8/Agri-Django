from django.urls import path,include
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('register/', views.register, name='register'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('profile/', views.profile, name='profile'),
    path('otp/', views.otp, name='otp'),
    path('challan/', views.challan, name='challan'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('admin/', include('admin_panel.urls')),  # this is for the admin panel
]