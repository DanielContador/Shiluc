from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from horas.models import Servicio
from rest_servicio.serializers import ServicioSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from horas.forms import ServicioForm

# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_servicio(request):
    datos = {
        'form':ServicioForm()
    }
    if request.method =='GET':
        listaServicio = Servicio.objects.all()
        serializer = ServicioSerializer(listaServicio, many = True)
        return render(request, 'horas/index.html', listaServicio)
    elif request.method == 'POST':
                #esto debe rescatarlo del form
        dataP = ServicioForm(request.POST)
        serializer = ServicioSerializer(data=dataP)
        if serializer.is_valid():
            serializer.save()
            datos['mensajeAPI'] = 'Guardado'
            return render(request, 'horas/agregarservicio.html', datos)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        





@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_servicio(request, id):
    try:
        servicio = Servicio.objects.get(id=id)
    except Servicio.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ServicioSerializer(servicio)
        return Response(serializer.data)
    elif request.method == "PUT":
        dataP = JSONParser().parse(request)
        serializer = ServicioSerializer(servicio, data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        servicio.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

