
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
    
    nombre = forms.CharField(label="Nombre")
    rut = forms.CharField(label="Rut")
    edad= forms.CharField(label="Edad")
    fecha = forms.DateField(label='Fecha de examen:', widget=forms.SelectDateWidget(years=range(1900,2022)))
    hemograma = forms.CharField(label="Hemograma")
    orina = forms.CharField(label="Orina")
    colesterolhdl = forms.CharField(label="HDL")
    colesterolldl = forms.CharField(label="LDL")
    glucosa = forms.CharField(label="Glucosa")
    
    nombre.widget.attrs.update({'class': 'form-control'})
    rut.widget.attrs.update({'class': 'form-control'})
    edad.widget.attrs.update({'class': 'form-control'})
    fecha.widget.attrs.update({'class': 'form-control'})
    hemograma.widget.attrs.update({'class': 'form-control'})
    orina.widget.attrs.update({'class': 'form-control'})
    colesterolhdl.widget.attrs.update({'class': 'form-control'})
    colesterolldl.widget.attrs.update({'class': 'form-control'})
    glucosa.widget.attrs.update({'class': 'form-control'})
    
    
