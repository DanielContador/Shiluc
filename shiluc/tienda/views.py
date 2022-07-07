from django.shortcuts import render
from .models import *

# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    context={'productos':productos}
    return render(request, 'tienda/tienda.html', context)


def carrito(request):
    context = {}
    return render(request, 'tienda/carrito.html', context)

def checkout(request):
    context={}
    return render(request, 'tienda/checkout.html', context)

def maintienda(request):
    context={}
    return render(request, 'tienda/main.html', context)

