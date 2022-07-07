from django.shortcuts import render
from .models import *

# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    context={'productos':productos}
    return render(request, 'tienda/tienda.html', context)


def carrito(request):
    
    if request.user.is_authenticated:
        cliente= request.user.cliente
        orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenproducto_set.all()
    else:
        items = []
        orden = {'get_cart_total':0, 'get_cart_items':0}
        
    context = {'items': items, 'orden':orden}
    return render(request, 'tienda/carrito.html', context)

def checkout(request):
    if request.user.is_authenticated:
        cliente= request.user.cliente
        orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenproducto_set.all()
        
    else:
        items = []
        orden = {'get_cart_total':0, 'get_cart_items':0}
    context={'items':items, 'orden':orden}
    return render(request, 'tienda/checkout.html', context)

def maintienda(request):
    context={}
    return render(request, 'tienda/main.html', context)

