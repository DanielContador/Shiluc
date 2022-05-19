from django.urls import URLPattern, path
from .views import eliminarservicio, index, contacto, iniciosesion, registro, agregarservicio, modificarservicio
from .import views
urlpatterns = [
    path('', index, name="index"),
    path('contacto/', views.contacto , name='contacto'),
    path('index/', views.index2 , name='index2'),
    path('iniciosesion/', views.iniciosesion , name='iniciosesion'),
    path('registro/', views.registro , name='registro'),
    path('agregarservicio/', views.agregarservicio , name='agregarservicio'),
    path('modificarservicio/<id>',views.modificarservicio, name='modificarservicio'),
    path('eliminarservicio/<id>', eliminarservicio, name='eliminarservicio'),
    
    ]



