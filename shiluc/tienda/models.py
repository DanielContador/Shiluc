from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    imagen = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.nombre
    ##property, hace que la pagina no se caiga si
    ##no se agrega una imagen al producto
    @property
    def imagenURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    id_transaccion = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id)
    
class OrdenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden,on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0, null=True,blank=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    
    
    #def?
    
    
class DireccionEnvio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
    direccion = models.CharField(max_length=200, null=False)
    ciudad = models.CharField(max_length=200, null=False)
    region = models.CharField(max_length=200, null=False)
    cpostal = models.CharField(max_length=200, null=False)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.direccion