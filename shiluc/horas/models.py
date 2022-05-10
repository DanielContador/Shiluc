from django.db import models
#makemigrations migrate: para crear tablas en base de datos
# Create your models here.
class Cliente(models.Model):
   
    nombreCliente = models.CharField(max_length=50,verbose_name='Nombre cliente', blank=False, null=False)
    nombreUsuario = models.CharField(max_length=16,verbose_name='Nombre Usuario', blank=False, null=False)
    correo = models.CharField(max_length=50,verbose_name='Correo', blank=False, null=False)
    telefono = models.IntegerField(verbose_name='teléfono', blank=False, null=False)
    claveUsuario = models.CharField(max_length=12,verbose_name='Contraseña', blank=False, null=False)
    


    def __str__(self):
        return self.nombreCliente


class Servicio(models.Model):
    
    tipoServicio = models.CharField(max_length=20, verbose_name='Tipo de servicio', blank=False, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipoServicio
