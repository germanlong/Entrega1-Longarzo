from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .forms import FormUsuario
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
    
    form_usuario = FormUsuario()
    
    return render(request, "formulario.html", {"form": form_usuario})


#print(request.GET)
    
    #nombre = request.GET.get("nombre")
    
    #nombre = Blog(nombre=request.GET.get("nombre"))
    #nombre.save()