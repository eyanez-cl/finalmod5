
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms.widgets import NullBooleanSelect
   
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
    edad = forms.IntegerField(label="Edad")
    fecha_nacimiento = forms.DateField(label="Fecha_naciemiento")
    
    
    
    nombre.widget.attrs.update({'class': 'form-control'})
    rut.widget.attrs.update({'class': 'form-control'})
    edad.widget.attrs.update({'class': 'form-control'})
    fecha_nacimiento.widget.attrs.update({'class': 'form-control'})
    
    
    
class FormularioPacientes(forms.Form):
    nombre = forms.CharField(validators=[validators.MinLengthValidator(2,"Su nombre debe poseer mas de 2 caracteres")])
    rut = forms.CharField()
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    hemograma =forms.IntegerField()
    orina = forms.IntegerField()
    colesterol_ldl = forms.IntegerField()
    colesterol_hdl = forms.IntegerField()
    glucosa = forms.IntegerField()
    
    '''
    nombre.widget.attrs.update({'class': 'form-control'})
    rut.widget.attrs.update({'class': 'form-control'})
    edad.widget.attrs.update({'class': 'form-control'})
    fecha_nacimiento.widget.attrs.update({'class': 'form-control'})
    fecha_toma_examen.widget.attrs.update({'class': 'form-control'})
    hemograma.widget.attrs.update({'class': 'form-control'})
    orina.widget.attrs.update({'class': 'form-control'})
    colesterol_ldl.widget.attrs.update({'class': 'form-control'})
    colesterol_hdl.widget.attrs.update({'class': 'form-control'})
    glucosa.widget.attrs.update({'class': 'form-control'})
   ''' 
    
    
    
    
    
    
