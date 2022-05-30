from rest_framework import serializers
from horas.models import Servicio


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['precio', 'nombreServicio', 'descripcion']