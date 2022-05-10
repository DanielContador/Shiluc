from django.shortcuts import render

# Create your views here.

# metodo constructor
class Persona:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
    #llama al init del padre
        super().__init__()
def index(request):
    persona1 = Persona("Asd asd", "21", "333222")
    lista= ["Pendulo", "Carta", "Lectura"]
    contexto = {"nombre":"Asd Asd", "servicios" : lista, "persona":persona1}
    return render(request, 'horas/index.html', contexto)
    


