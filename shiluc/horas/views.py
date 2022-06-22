from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Perfil
from .forms import SignUpForm
from .models import Servicio
from django.contrib.auth.views import LoginView, LogoutView

from .forms import ServicioForm

# Create your views here.
#EJEMPLOS EN CLASES
#def index(request):
    #persona1 = Persona("Asd asd", "21", "333222")
    #lista= ["Pendulo", "Carta", "Lectura"]
    #contexto = {"nombre":"Asd Asd", "servicios" : lista, "persona":persona1}
    #return render(request, 'horas/index.html', contexto)

# metodo constructor
#class Persona:
    #def __init__(self, nombre, edad, telefono):
        #self.nombre = nombre
        #self.edad = edad
        #self.telefono = telefono
    #llama al init del padre
        #super().__init__()
 #-----------------------------------------------------------------------------------------------------       
def index(request):
    servicios = Servicio.objects.all()
    datos = {

        'servicios': servicios
    }

    return render(request, 'horas/index.html', datos)



def contacto(request):
    return render(request, 'horas/contacto.html')

def base(request):
    return render(request, 'horas/base.html')

def index2(request):
    return render(request, 'horas/index.html')

def iniciosesion(request):
    return render(request, 'horas/iniciosesion.html')

def registro(request):
    return render(request, 'horas/formu.html')

def agregarservicio(request):
    datos = {
    'form':ServicioForm()
    }

    if(request.method == 'POST'):
        formulario = ServicioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado correctamente'


    return render(request,'horas/agregarservicio.html',datos)


def modificarservicio(request, id):
    servicio=Servicio.objects.get(id=id)


    datos= {
        'form':ServicioForm(instance=servicio)
    }


    if(request.method == 'POST'):
        formulario = ServicioForm(data=request.POST, instance=servicio)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificado correctamente'

    return render(request, 'horas/modificarservicio.html', datos)


def eliminarservicio(request, id):
    servicio=Servicio.objects.get(id=id)
    servicio.delete()

    return redirect(to='index')

    
class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('index')

class BienvenidaView(TemplateView):
   template_name = 'horas/bienvenida.html'


class SignInView(LoginView):
    template_name = 'horas/iniciar_sesion.html'
    
    
class SignOutView(LogoutView):
    pass