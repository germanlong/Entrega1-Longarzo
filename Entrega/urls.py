from django.urls import path
from .views import vista_1, vista_2, listado_nombres

urlpatterns = [
    path('', vista_1, name="index"),
    path('nombres/', listado_nombres, name="listado_nombres"),
    path('Crear/', vista_2, name="crear"),
    
]