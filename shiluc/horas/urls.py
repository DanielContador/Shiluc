from django.urls import URLPattern, path, include
from .views import eliminarservicio, index, contacto, iniciosesion, registro, agregarservicio, modificarservicio, base
from .import views
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
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    
    ]



