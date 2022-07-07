from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

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

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:',productId)
    
    cliente = request.user.cliente
    producto = Producto.objects.get(id=productId)
    orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
    ordenproducto, created = OrdenProducto.objects.get_or_create(orden=orden, producto=producto)
    
    if action =='add':
        ordenproducto.cantidad = (ordenproducto.cantidad + 1)
    elif action =='remove':
        ordenproducto.cantidad = (ordenproducto.cantidad - 1)
    
    ordenproducto.save()
    
    if ordenproducto.cantidad<=0:
        ordenproducto.delete()
        
    return JsonResponse('Producto fue añadido', safe=False)

