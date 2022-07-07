from django.urls import path
from . import views


urlpatterns = [
    path('tienda/', views.tienda, name="tienda"),
    path('maintienda/', views.maintienda, name="maintienda"),
    path('carrito/', views.carrito, name="carrito"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]   
