from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Blog

# Create your views here.

def vista_1(request):
    return render(request, "index.html")

def vista_2(request):
    
    blog1 = Blog(nombre="Carlos") 
    blog2 = Blog(nombre="Juan") 
    blog3 = Blog(nombre="Pepe")  

    return render(request, "mi_template.html", {"lista_objetos": [blog1, blog2, blog3]})