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
    path('agregarusuario/', views.agregar_usuario,name='agregar_usuario')
    
]
