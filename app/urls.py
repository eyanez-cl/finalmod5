from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('login/',views.login_user,name='login'),
    path('private/', views.private,name='private'),
    path('graficos/', views.graficos,name='graficos'),
    path('crearexamen/', views.crear_examen,name='crearexamen'),
    path('examenes/', views.listar_examenes,name='examenes'),
    path('agendar/', views.agendar,name='agendar'),
    path('agregar_usuario/', views.agregar_usuario,name='agregar_usuario'),
     path('agregar_usuario_exitoso/', 
          views.agregar_usuario_exitoso,
          name='agregar_usuario_exitoso'),
]
