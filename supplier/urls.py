from django.urls import path

from . import views

urlpatterns = [
    path('supplier_dashboard/', views.supplier_dashboard, name='supplier_dashboard'),
    path('create_commodity/', views.create_commodity, name='create_commodity'),
    path('request_supply_tender/', views.request_supply_tender, name='request_supply_tender'),
    path('supply_requests/', views.supply_requests, name='supply_requests'),
    path('rejected_supply_requests/', views.rejected_supply_requests, name='rejected_supply_requests'),
    path('approved_supply_requests/', views.approved_supply_requests, name='approved_supply_requests'),
    path('pending_supply_requests/', views.pending_supply_requests, name='pending_supply_requests'),
    path('request_detail/<int:request_id>/', views.request_detail, name='request_detail'),
]