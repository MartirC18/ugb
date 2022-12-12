from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CLIENTES

def index(request):
    return render(request,'index.html')

def adminclientes(request):
    clientes=CLIENTES.objects.all()
    return render(request,'registro.html',{"clientes":clientes})
    
def agregarclientes(request):
    nombre=request.POST['inputnombre']
    telefono=request.POST['inputtelefono']
    direccion=request.POST['inputdireccion']
    sexo=request.POST['inputsexo']
    
    clientes=CLIENTES.objects.create(
        Nombre_Cliente=nombre,Telefono=telefono,Direccion=direccion,Sexo=sexo
    )
    return redirect('/registro')
    