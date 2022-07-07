from django.urls import path
from . import views


urlpatterns = [
    path('tienda/', views.tienda, name="tienda"),
    path('maintienda/', views.maintienda, name="maintienda"),
    path('carrito/', views.carrito, name="carrito"),
    path('checkout/', views.checkout, name="checkout"),
]
