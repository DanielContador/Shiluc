from django.urls import URLPattern, path, include
from .views import eliminarservicio, index, contacto, iniciosesion, registro, agregarservicio, modificarservicio, base
from .import views
from horas.views import SignUpView, BienvenidaView, SignInView, SignOutView
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
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
    path('base/', views.base, name='base'),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    
    ]



