from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ProductsForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    producto_cards = Producto.objects.order_by('-id')[0:3]
    producto_list = Producto.objects.order_by('-id')[3:10]

#Buscador
    queryset = request.GET.get("item_name")
    producto_objects = Producto.objects.all()
    if queryset:
        producto_cards = Producto.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(detalles__icontains = queryset)
        ).distinct()

    return render(request,'Tienda/index.html',{'producto_cards':producto_cards,'producto_list':producto_list,'producto_objects':producto_objects,
        "lista_secciones": Seccion.objects.all(),
        "lista_articulos": Producto.objects.all(),})

def detalle(request,id):
    producto_object = Producto.objects.get(id=id)
    return render(request,'Tienda/detalle.html', {'producto_object':producto_object})

def order(request):

    if request.method == "POST":
        items = request.POST.get('items','')
        nombre = request.POST.get('nombre',"")
        domicilio = request.POST.get('domicilio',"")
        ciudad = request.POST.get('ciudad',"")
        cpostal = request.POST.get('cpostal',"")
        total = request.POST.get('total',"")

        order = Order(items=items,nombre=nombre,domicilio=domicilio,ciudad=ciudad,cpostal=cpostal,total=total)
        order.save()


    return render(request,'Tienda/carrito.html')

def filtro_secciones(request, seccion_id):
    una_seccion = get_object_or_404(Seccion, id=seccion_id)
    queryset = Producto.objects.all()
    queryset = queryset.filter(seccion=una_seccion)
    return render(request,"Tienda/index.html", {
        "producto_cards": queryset,
        "lista_secciones": Seccion.objects.all(),
        "seccion_seleccionada": una_seccion
    })



def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'registration/register.html',data)

def agregar(request):

    data = {
        'form': ProductsForm()
    }

    if request.method == "POST":
        formulario = ProductsForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'Tienda/producto/agregar.html',data)

def modificar(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductsForm(instance=producto)
    }

    if request.method == "POST":
        formulario = ProductsForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'Tienda/producto/modificar.html', data)

def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="index")

def acerca(request):
    return render(request,'Tienda/acerca.html')