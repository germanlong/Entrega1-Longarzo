from django import forms

class FormUsuario(forms.Form):
    nombre = forms.CharField(max_length=30)
    
class Busqueda(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
