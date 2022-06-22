from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#makemigrations migrate: para crear tablas en base de datos
#pip install pillow (image field)
# Create your models here.


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    fotoPerfil = models.ImageField(upload_to='fotosPerfil', height_field=None, width_field=None, max_length=100, null=True)
    
    def __str__(self):
        return self.usuario.username
    
@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()
    


class Servicio(models.Model):
    precio = models.IntegerField(verbose_name='Precio', default=0)
    nombreServicio = models.CharField(max_length=20, verbose_name='Tipo de servicio')
    descripcion = models.CharField(max_length=50,verbose_name='Descripción', null=True)

    def __str__(self):
        return self.nombreServicio

class Reserva(models.Model):
    
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    fechaReserva = models.DateTimeField(null=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=50,verbose_name='Comentario')
    def __str__(self):
        return self.comentario
