from django.contrib import admin
from .models import Perfil, Servicio, Reserva
# Register your models here.

#Holaholahola123 correo: aaa@aaa.aaa username: 123

admin.site.register(Servicio)
admin.site.register(Reserva)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio')