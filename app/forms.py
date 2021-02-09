
from django import forms
from django.core import validators

   
class Login(forms.Form):
     
    email = forms.EmailField(required=False)
    clave = forms.CharField(label='Contraseña',required=False,widget = forms.PasswordInput())
   
    email.widget.attrs.update({'class': 'form-control'})
    clave.widget.attrs.update({'class': 'form-control'})
    
    
class Examen(forms.Form):
    
    # nombre = forms.CharField(label="Nombre")
    # rut = forms.CharField(label="Rut")
    # examen = forms.CharField(label="Examen")
    # medico = forms.CharField(label="Medico")
    

    nombre = forms.CharField(label="nombre")
    rut = forms.CharField(label="Rut")
    examen = forms.CharField(label="Examen")
    medico = forms.CharField(label="Medico")
    
    nombre.widget.attrs.update({'class': 'form-control'})
    rut.widget.attrs.update({'class': 'form-control'})
    examen.widget.attrs.update({'class': 'form-control'})
    medico.widget.attrs.update({'class': 'form-control'})
    
    
