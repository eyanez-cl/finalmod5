import json


from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import Login, Examen, FormularioPacientes


# Create your views here.

def buscar(email,clave,usuarios):
    for item in usuarios['usuarios']:
        if item['email'] == email and item['clave'] == clave:
            return True
    
def inicio(request):
    if request.method == "GET":
        formulario = Login(request.GET)   
        
        context = {'formulario':formulario}
    return render(request,'app/index.html',context)


def login_user(request):
    if request.method == "POST":
        formulario_lleno = Login(request.POST)
        if formulario_lleno.is_valid() == True:
            data = formulario_lleno.cleaned_data
            filename = "/app/data/usuarios.json"
            with open(str(settings.BASE_DIR)+filename,'r') as file:
                contactos = json.load(file)   
            validar = buscar(data['email'],data['clave'],contactos)
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
    # if request.method == "GET":
    #     formulario = Examen(request.GET)   
    #     context = {'formulario':formulario}    
        return render(request,'app/Examenes.html')




    # if request.method == "POST":
    #     formulario_lleno = Examen(request.POST)
    #     if formulario_lleno.is_valid() == True:
    #         data = formulario_lleno.cleaned_data
    #         filename = "/app/data/examenes.json"
    #         with open(str(settings.BASE_DIR)+filename,'w') as file:
    #             pass
                
        
def agendar(request):
    return render(request,'app/Agendar.html')


def crear_examen(request):
    data = dict() # pa meter cosas 
    
    if request.method == 'POST':
        formulario = Examen(request.POST)
        if formulario.is_valid():
            #hacer algoooo Lista de examenes formulario_clean_data
            data['formulario_is_valid'] = True
            data['html_examenes_list '] = render_to_string('app/Examen_lista _parcial.html',{'lista_examenes': lista_examenes })            
        else:
            data['formulario_is_valid'] = False
            
    else:
        formulario = Examen()
        print(dir(formulario))
        context = {'formulario': formulario}
        data['html_formulario'] = render_to_string('app/Examen_parcial.html',
                                 context,
                                 request = request,
                                 )
    return JsonResponse(data)


#def agregar_usuario(request):
    data = dict() # pa meter cosas 
    
    if request.method == 'POST':
        formulario = FormularioPacientes(request.POST)
        if formulario.is_valid():
            #hacer algoooo Lista de examenes formulario_clean_data
            data['formulario_is_valid'] = True
            data['html_usuarios_list '] = render_to_string('app/usuario_lista _parcial.html',{'lista_usuarios': lista_usuarios })            
        else:
            data['formulario_is_valid'] = False
            
    else:
        formulario = FormularioPacientes()
        print(dir(formulario))
        context = {'formulario': formulario}
        data['html_formulario'] = render_to_string('app/usuario_parcial.html',
                                 context,
                                 request = request,
                                 )
    return JsonResponse(data)



def context_lista_pacientes():
    filename = "/app/data/pacientes.json"
    with open(str(settings.BASE_DIR) + filename, 'r') as file:
        pacientes = json.load(file)
    context= {'lista_pacientes': pacientes['pacientes']}
    return context
    

def agregar_usuario(request):
    
    if request.method == 'GET':
        formulario = FormularioPacientes()
        context = {'formulario': formulario}
        context.update(context_lista_pacientes())
        print(context)
        return render(request,'app/Agregar_usuario.html',context)

    elif request.method == 'POST':
        print('El post contiene:', request.POST)
        
        formulario_devuelto = FormularioPacientes(request.POST)
        
        if formulario_devuelto.is_valid() == True:
            datos_formulario = formulario_devuelto.cleaned_data
            datos_formulario['fecha_nacimiento']= datos_formulario['fecha_nacimiento'].strftime("%Y-%m-%d")
            
            print ('los datos limpios del formulario son: ', datos_formulario)
            filename = '/app/data/pacientes.json'
            with open(str(settings.BASE_DIR)+ filename, 'r') as file:
                data= json.load(file)
                data['pacientes'].append(datos_formulario)
            with open(str(settings.BASE_DIR)+ filename, 'w') as file:
                json.dump(data, file)
                
            return redirect('app:agregar_usuario')
            #return render(request, 'app/agregar_usuario_exitoso.html', context) 
        else:
            context= {'formulario': formulario_devuelto}
            context.update(context_lista_pacientes())
            return render(request, 'app/Agregar_usuario.html', context)
        


def lista_pacientes(request):
    context = context_lista_pacientes()
    return render( request, 'app/Agregar_usuario.html', context)


def eliminar_pacientes(request, rut):
    if request.method == 'GET':
        context = {'rut': rut}
        return render(request, 'app/eliminar_pacientes.html', context)
    
    if request.method == 'POST':
        filename = "/app/data/pacientes.json"
        with open(str(settings.BASE_DIR) + filename, 'r') as file:
            data = json.load(file)
        for paciente in data['pacientes']:
            if str(paciente['rut']) == str(rut):
                data['pacientes'].remove(paciente)
                break
            with open(str(settings.BASE_DIR) + filename, 'w') as file:
                json.dump(data, file)
                
            return redirect('app:lista_pacientes')

    