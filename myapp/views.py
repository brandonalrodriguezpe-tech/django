from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# 1. MÓDULO PÚBLICO: Catálogo de libros abierto para todos
def catalogo_libros(request):
    libros = [
        {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True},
        {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "disponible": False},
        {"titulo": "El coronel no tiene quien le escriba", "autor": "Gabriel García Márquez", "disponible": True}
    ]
    return render(request, 'catalogo.html', {'libros': libros})

# 2. MÓDULO PRIVADO 1: Historial de préstamos (Requiere Login)
@login_required
def mis_prestamos(request):
    return render(request, 'prestamos.html')

# 3. MÓDULO PRIVADO 2: Panel de administración para agregar libros (Requiere Login de Admin)
@login_required
def agregar_libro(request):
    if not request.user.is_staff:
        return redirect('catalogo')
    return render(request, 'agregar.html')



