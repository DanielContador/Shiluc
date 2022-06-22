from django.urls import URLPattern, path
from .views import eliminarservicio, index, contacto, iniciosesion, registro, agregarservicio, modificarservicio
from .import views
from horas.views import SignUpView, BienvenidaView, SignInView, SignOutView
urlpatterns = [
    path('', index, name="index"),
    path('contacto/', views.contacto , name='contacto'),
    path('index/', views.index2 , name='index2'),
    path('iniciosesion/', views.iniciosesion , name='iniciosesion'),
    path('registro/', views.registro , name='registro'),
    path('agregarservicio/', views.agregarservicio , name='agregarservicio'),
    path('modificarservicio/<id>',views.modificarservicio, name='modificarservicio'),
    path('eliminarservicio/<id>', eliminarservicio, name='eliminarservicio'),
    path('', BienvenidaView.as_view(), name='bienvenida'),
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('incia-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
    
    ]



