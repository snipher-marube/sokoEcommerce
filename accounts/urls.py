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
]