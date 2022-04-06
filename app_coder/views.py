import string
from django.shortcuts import render
from django.template import Template, Context, loader
from app_coder.models import Usuario, Administrador, Comentario
from app_coder.forms import UsuarioFormulario, Buscar_usuario, Comentarioform

def inicio(request):
    comentarios = Comentario.objects.values()
    comentarios = {'comentarios':list(comentarios)}
    return render(request, "app_coder/index.html", comentarios)

def crear_cuenta(request):
    if request.method == "POST":
        usuario = UsuarioFormulario(request.POST)
        if usuario.is_valid():
            data = usuario.cleaned_data
            usuario_nuevo = Usuario(data['nombre'], data['password'], data['email'])
            usuario_nuevo.save()
        return render(request, "app_coder/comentario.html")
    else:
        miFormulario = UsuarioFormulario()
        return render(request, "app_coder/inisecion.html", {'formulario': miFormulario})

def administrador_iniciar_sesion(request):
    if request.method == "POST":
        usuario = UsuarioFormulario(request.POST)
        if usuario.is_valid():
            data = usuario.cleaned_data
            usuario_nuevo = Administrador(data['nombre'], data['password'], data['email'])
            usuario_nuevo.save()
        return render(request, "app_coder/buscar.html")
    else:
        return render(request, "app_coder/inisecion-admin.html")

def publicar(request):
    if request.method == "POST":
        comentario = Comentarioform(request.POST)
        if comentario.is_valid():
            data = comentario.cleaned_data
            comentario_nuevo = Comentario(data['titulo'], data['mensaje'], data['creador'])
            comentario_nuevo.save()
        comentarios = Comentario.objects.values()
        comentarios = {'comentarios':list(comentarios)}
        return render(request, "app_coder/index.html", comentarios)
    else:
        return render(request, "app_coder/comentario.html")

def buscar_usuario(request):
    if request.method == "POST":
        busqueda = Buscar_usuario(request.POST)
        if busqueda.is_valid():
            data = busqueda.cleaned_data
            usuarios = Usuario.objects.filter(nombre=data['nombre'])
            return render(request, "app_coder/buscar.html", {"buscando": True, "usuarios": usuarios})
    else:
        if(request.method == 'GET'):
            print(request.GET)
            usu = request.GET
            usu = list(usu.keys())[0]
            borusu = Usuario.objects.get(nombre=usu)
            borusu.delete()
        return render(request, "app_coder/buscar.html",{"buscando": False, "usuarios": ""})
