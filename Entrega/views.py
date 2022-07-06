from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .forms import Busqueda, FormUsuario
from .models import Blog

# Create your views here.

def vista_1(request):
    return render(request, "index.html")

def vista_2(request):
    
    if request.method == "POST": 
        form = FormUsuario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            nombre = Blog(
                nombre=data.get("nombre"),
            )
            nombre.save()
            
            listado_nombres = Blog.objects.all()
            form = Busqueda()
            
            return render(request, "listado_nombres.html", {"listado_nombres" : listado_nombres, "form":form})
        
        else: 
            return render(request, "formulario.html", {"form": form})
    
    form_usuario = FormUsuario()
    
    return render(request, "formulario.html", {"form": form_usuario})


def listado_nombres(request):
    
    nombre_de_busqueda = request.GET.get("nombre")
    
    if nombre_de_busqueda:
        listado_nombres = Blog.objects.filter(nombre__icontains=nombre_de_busqueda)
    else:
        listado_nombres = Blog.objects.all()
        
    form = Busqueda()
    return render(request, "listado_nombres.html", {"listado_nombres" : listado_nombres, "form" : form})