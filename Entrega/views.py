from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Blog

# Create your views here.

def vista_1(request):
    return HttpResponse ("<h1>Blog Py</h1>")

def vista_2(request):
    
    #template = loader.get_template("index.html")
    
    blog1 = Blog(nombre="Carlos") 
    blog2 = Blog(nombre="Juan") 
    blog3 = Blog(nombre="Pepe")  
      
    #render = template.render({"lista_objetos": [blog1, blog2, blog3]})
    
    #return HttpResponse (render)

    return render(request, "index.html", {"lista_objetos": [blog1, blog2, blog3]})