from django.contrib import admin
from django.urls import path
from miaplicación import views  # Importa las vistas de tu app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.catalogo_libros, name='catalogo'),               # Módulo Público
    path('mis-prestamos/', views.mis_prestamos, name='prestamos'),    # Módulo Privado 1
    path('nuevo-libro/', views.agregar_libro, name='agregar'),        # Módulo Privado 2
]
