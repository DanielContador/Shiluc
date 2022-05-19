from django.db import models
#makemigrations migrate: para crear tablas en base de datos
#pip install pillow (image field)
# Create your models here.
class Cliente(models.Model):
   
    nombreCliente = models.CharField(max_length=50,verbose_name='Nombre cliente')
    nombreUsuario = models.CharField(max_length=16,verbose_name='Nombre Usuario')
    correo = models.CharField(max_length=50,verbose_name='Correo')
    telefono = models.IntegerField(verbose_name='teléfono')
    claveUsuario = models.CharField(max_length=12,verbose_name='Contraseña')
    imagenUsuario = models.ImageField(upload_to='ImagenUsuario', height_field=None, width_field=None, max_length=100, null=True)
    


    def __str__(self):
        return self.nombreCliente


class Servicio(models.Model):
    precio = models.IntegerField(verbose_name='Precio', default=0)
    nombreServicio = models.CharField(max_length=20, verbose_name='Tipo de servicio')
    descripcion = models.CharField(max_length=50,verbose_name='Descripción', null=True)

    def __str__(self):
        return self.nombreServicio

class Reserva(models.Model):
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fechaReserva = models.DateTimeField(null=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=50,verbose_name='Comentario')
    def __str__(self):
        return self.comentario
