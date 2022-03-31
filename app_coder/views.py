from django.shortcuts import render
from django.template import Template, Context, loader
from app_coder.models import Usuario, Administrador, Comentario
from app_coder.forms import UsuarioFormulario

def inicio(request):
    return render(request, "app_coder/index.html")

def crear_cuenta(request):
    if request.method == "POST":
        usuario = UsuarioFormulario(request.POST)
        if usuario.is_valid():
            data = usuario.cleaned_data
            usuario_nuevo = Usuario(data['nombre'], data['password'], data['email'])
            usuario_nuevo.save()
            return render(request, " ")
    else:
        miFormulario = UsuarioFormulario()
        return render(request, "app_coder/inisecion.html", {'formulario': miFormulario})

def administrador_iniciar_sesion(request):
    pass

def publicar(request):
    pass

def buscar_usuario(request):
    pass
