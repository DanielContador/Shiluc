from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime

# Create your views here.

def tienda(request):
    
    if request.user.is_authenticated:
        cliente= request.user.cliente
        orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_cart_items
    else:
        items = []
        orden = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = orden['get_cart_items']
        
    productos = Producto.objects.all()
    context={'productos':productos, 'cartItems':cartItems}
    return render(request, 'tienda/tienda.html', context)


def carrito(request):
    
    if request.user.is_authenticated:
        cliente= request.user.cliente
        orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_cart_items
    else:
        items = []
        orden = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = orden['get_cart_items']
    context = {'items': items, 'orden':orden, 'cartItems': cartItems}
    return render(request, 'tienda/carrito.html', context)
#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
def checkout(request):
    if request.user.is_authenticated:
        cliente= request.user.cliente
        orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_cart_items
        
    else:
        items = []
        orden = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = orden['get_cart_items']
    context={'items':items, 'orden':orden, 'cartItems':cartItems}
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

#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
def processOrder(request):
    id_transaccion= datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        cliente=request.user.cliente
        orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
        total=int(data['form']['total'])
        orden.id_transaccion = id_transaccion
        
        if total ==int(orden.get_cart_total):
            orden.completado = True
        orden.save()
        
        
        if orden.shipping==True:
            DireccionEnvio.objects.create(
            cliente=cliente,
            orden=orden,
            direccion=data['shipping']['address'],
            ciudad=data['shipping']['city'],
            region=data['shipping']['state'],
            cpostal=data['shipping']['zipcode'],
            )
    else:
        print('Usuario no esta registrado...')
    return JsonResponse('Pago completado', safe=False)