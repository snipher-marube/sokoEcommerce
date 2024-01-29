from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),

    path('forgot-password/', views.forgotPassword, name='forgotPassword'),
    path('reset-password-validate/<uidb64>/<token>/', views.resetPasswordValidate, name='resetPasswordValidate'),
    path('reset-password/', views.resetPassword, name='resetPassword'),

    path('my_orders/', views.my_orders, name='my_orders'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('order_details/<int:order_id>/', views.order_detail, name='order_detail'),

    path('registerVendor/', views.registerVendor, name='registerVendor'),
    path('loginVendor/', views.loginVendor, name='loginVendor'),
    path('product-request/', views.product_request, name='product_request'),
]