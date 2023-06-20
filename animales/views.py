from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm, RegistroUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def qsomos(request):
    return render(request, 'qsomos.html')

def productos(request):
    return render(request, 'productos.html')

def contactanos(request):
    return render(request,'contactanos.html')

def carrito(request):
    return render(request,'carrito.html')

def registrar(request):
    data ={
        'form' : RegistroUserForm()
    }
    if request.method== "POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente!")
            return redirect('inicio')
        data["form"] = formulario       #sobreescribimos el form
    return render(request, 'registration/registro.html', data)


@login_required
def crear(request):
    if request.method=="POST":
        productoform = ProductoForm(request.POST,request.FILES) #creamos un objeto de tipo form para vehiculos
        if productoform.is_valid():
            productoform.save() #similar en funcion al metodo insert
            return redirect ('gestion')
    else:
        productoform=ProductoForm()
    return render(request, 'crear.html', {'productoform' : productoform})
    
@login_required
def eliminar(request, id):
    productoEliminado=Producto.objects.get(id=id) #buscamos un vehiculo por la patentes
    productoEliminado.delete()
    return redirect('gestion')

@login_required
def modificar(request,id):
    productoModificado = Producto.objects.get(id=id)
    datos ={
        'form': ProductoForm(instance=productoModificado)   #el objeto form llega al template
    }
    if request.method=="POST":          #modificamos backend con los cambios realizagestion
        formulario = ProductoForm(request.POST, request.FILES, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()           #modificamos el objeto
            return redirect('gestion')
    return render(request,'modificar.html', datos)





def gestion(request):
    productos=Producto.objects.raw('select * from animales_producto')
    datos={'productos':productos}
    return render(request, 'gestion.html', datos)



def productos(request):
    productos=Producto.objects.all()
    datos={
        'productos':productos
    }
    return render(request,'productos.html', datos)


