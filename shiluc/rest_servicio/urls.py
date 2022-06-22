from unicodedata import name
from django.urls import path
from rest_servicio.views import lista_servicio, detalle_servicio
from rest_servicio.viewsLogin import login

urlpatterns = [
    path('lista_servicio',lista_servicio,name="lista_servicio"),
    path('detalle_servicio/<id>', detalle_servicio, name='detalle_servicio'),
    #el del name es el que se utiliza en el html, el del medio es el que llama a la funcion de viewsLogin
    path('login',login,name='login'),

]