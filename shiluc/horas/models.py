from django.db import models
#makemigrations migrate: para crear tablas en base de datos
# Create your models here.
class Cliente(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    nombreCliente = models.CharField(max_length=50,verbose_name='Cliente', blank=False, null=False)
    nombreUsuario = models.CharField(max_length=16,verbose_name='Nombre Usuario', blank=False, null=False)
    correo = models.CharField(max_length=50,verbose_name='correo', blank=False, null=False)
    telefono = models.IntegerField(verbose_name='telefono', blank=False, null=False)
    claveUsuario = models.CharField(max_length=12,verbose_name='claveUsuario', blank=False, null=False)
    


    def __str__(self):
        return self.nombreCliente


class Servicio(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    tipoServicio = models.CharField(max_length=20, verbose_name='tipoServicio', blank=False, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipoServicio
