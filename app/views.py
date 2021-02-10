import json


from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import Login, Examen


# Create your views here.

def buscar(email,clave,pacientes):
    for item in pacientes:
        print(item['correo'],item['clave'])
        if item['correo'] == email and item['clave'] == clave:
            return True
        
def inicio(request):
    if request.method == "GET":
        formulario = Login(request.GET)   
        
        context = {'formulario':formulario}
    return render(request,'app/index.html')


def login_user(request):
    if request.method == "POST":
        formulario_lleno = Login(request.POST)
        if formulario_lleno.is_valid() == True:
            data = formulario_lleno.cleaned_data
            print(data)
            filename = "/app/data/base.json"
            with open(str(settings.BASE_DIR)+filename,'r') as file:
                pacientes = json.load(file)   
            validar = buscar(data['email'],data['clave'],pacientes['pacientes'])
            if validar == True:
                return redirect('app:private')
            else:
                formulario_lleno = Login()
                return redirect('app:inicio')               
        else:
            formulario_lleno = Login()
            return redirect('app:inicio')

def private(request):
    
    return render(request,'app/Privada.html')

def graficos(request):
    return render(request,'app/Graficos.html')

def listar_examenes(request):
    filename = "/app/data/base.json"
    with open(str(settings.BASE_DIR)+filename,'r') as file:
        pacientes = json.load(file)
        context = {"lista_examenes": pacientes['pacientes']}
    # if request.method == "GET":
    #     formulario = Examen(request.GET)   
    #     context = {'formulario':formulario}  
      
        return render(request,'app/Examenes.html',context)

def crear_examen(request):
    data = dict() # pa meter cosas 
    
    if request.method == 'POST':
        formulario = Examen(request.POST)
        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data
            datos_formulario['fecha'] = datos_formulario['fecha'].strftime("%Y-%m-%d")
            filename = "/app/data/base.json"
            with open(str(settings.BASE_DIR)+filename,'r') as file:
                pacientes = json.load(file)
                pacientes['pacientes'].append(datos_formulario)
            
            with open(str(settings.BASE_DIR)+filename,'w') as file:
                 json.dump(pacientes,file)
            
           
            print(datos)
            data['formulario_is_valid'] = True
            data['html_examenes_list '] = render_to_string('app/Examenes_lista_parcial.html',{
                'lista_examenes': pacientes['pacientes']
                })      
            #print(data)
            
        else:
            data['formulario_is_valid'] = False
            
    else:
        formulario = Examen()
    
    
    context = {'formulario': formulario}
    data['html_formulario'] = render_to_string('app/Examen_parcial.html',
                                               context,
                                               request = request,                                           )
    return JsonResponse(data)


    # if request.method == "POST":
    #     formulario_lleno = Examen(request.POST)
    #     if formulario_lleno.is_valid() == True:
    #         data = formulario_lleno.cleaned_data
    #         filename = "/app/data/examenes.json"
    #         with open(str(settings.BASE_DIR)+filename,'w') as file:
    #             pass
                
        
def agendar(request):
    return render(request,'app/Agendar.html')


def agregar_usuario(request):
    
    return render(request,'app/Agregar_usuario.html')