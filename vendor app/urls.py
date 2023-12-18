# vendor_management_project/vendor_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('vendors', views.create_vendor, name='create_vendor'),
    path('vendors/', views.list_vendors, name='list_vendors'),
    path('vendors/<int:vendor_id>/', views.get_vendor, name='get_vendor'),
    path('vendors/<int:vendor_id>', views.update_vendor, name='update_vendor'),
    path('vendors/del/<int:vendor_id>/', views.delete_vendor, name='delete_vendor'),

    path('purchase_orders', views.create_purchase_order, name='create_purchase_order'),
    path('purchase_orders/', views.list_purchase_orders, name='list_purchase_orders'),
    path('purchase_orders/<int:po_id>/', views.get_purchase_order, name='get_purchase_order'),
    path('purchase_orders/<int:po_id>', views.update_purchase_order, name='update_purchase_order'),
    path('purchase_orders/del/<int:po_id>/', views.delete_purchase_order, name='delete_purchase_order'),
    #path('vendors/<int:vendor_id>/performance/', views.get_vendor_performance, name='get_vendor_performance'),
    #path('purchase_orders/<int:po_id>/acknowledge/', views.acknowledge_purchase_order, name='acknowledge_purchase_order'),
    



    path('vendors', views.vendor_form, name='create_vendor_form'),
    path('vendors/', views.vendor_list, name='vendor_list'),
    path('vendors/<int:vendor_id>/', views.vendor_detail, name='vendor_detail'),
    path('vendors/<int:vendor_id>/update/', views.vendor_form, name='update_vendor_form'),

     
]
    
