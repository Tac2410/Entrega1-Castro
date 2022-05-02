from distutils import errors
import string
from urllib import request
from django.shortcuts import render
from django.template import Template, Context, loader
from app_coder.models import Comentario
from app_coder.forms import Comentarioform
from accounts.models import Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

def inicio(request):
    return render(request, "app_coder/inicio.html")

#def crear_cuenta(request):
#    if request.method == "POST":
#        usuario = FormcrearUsu(request.POST)
#        if usuario.is_valid():
#            data = usuario.cleaned_data['username']
#            usuario.save()
#            return render(request, "app_coder/mensajes.html", {"mensaje": "Usuario Creado"})
#        else:
#            return render(request, "app_coder/mensajes.html", {"mensaje": "No paso la validacion"})
#    else:
#        miFormulario = FormcrearUsu()
#        return render(request, "app_coder/crearcuenta.html", {'formulario': miFormulario})

#def login_rec(request):
#    if request.method == "POST":
#        usuario = AuthenticationForm(request, data=request.POST)
#        if usuario.is_valid():
#            usu = usuario.cleaned_data.get('username')
#            con = usuario.cleaned_data.get('password')

#            user = authenticate(username=usu, password=con)
#
#            if user is not None:
#                login(request, user)
#                return render (request, "app_coder/mensajes.html", {"mensaje":f"Bienvenido {usu}"})
#            else:
#                return render (request, "app_coder/mensajes.html", {"mensaje":"Error, datos incorrectos"})
#        else:
#            return render (request, "app_coder/mensajes.html", {"mensaje":"Error, formulario erroneo"})
#    else:
#        miFormulario = AuthenticationForm()
#        return render(request, "app_coder/login.html", {'formulario': miFormulario})

#def administrador_iniciar_sesion(request):
#    if request.method == "POST":
#        usuario = UsuarioFormulario(request.POST)
#        if usuario.is_valid():
#            data = usuario.cleaned_data
#            usuario_nuevo = Administrador(data['nombre'], data['password'], data['email'])
#            usuario_nuevo.save()
#        return render(request, "app_coder/buscar.html")
#    else:
#        miFormulario = UsuarioFormulario()
#        return render(request, "app_coder/inisecion-admin.html", {'formulario': miFormulario})

@login_required()
def publicar(request):
    if request.method == "POST":
        comentario = Comentarioform(request.POST, request.FILES)
        if comentario.is_valid():
            username = request.user.username
            data = comentario.cleaned_data
            comentario_nuevo = Comentario(data['titulo'], data['subtitulo'], data['cuerpo'], username, data['imagen'])
            comentario_nuevo.save()
        return render(request, "app_coder/inicio.html")
    else:
        miFormulario = Comentarioform()
        return render(request, "app_coder/comentario.html", {'formulario': miFormulario})

#def buscar_usuario(request):
#    if request.method == "POST":
#        busqueda = Buscar_usuario(request.POST)
#        if busqueda.is_valid():
#            data = busqueda.cleaned_data
#            usuarios = Usuario.objects.filter(nombre=data['nombre'])
#            return render(request, "app_coder/buscar.html", {"buscando": True, "usuarios": usuarios})
#    else:
#        if(request.method == 'GET'):
#            usu = request.GET
#            usu = list(usu.keys())[0]
#            borusu = Usuario.objects.get(nombre=usu)
#            borusu.delete()
#        return render(request, "app_coder/buscar.html",{"buscando": False, "usuarios": ""})

#@login_required()
#def actualizar_usuario(request):
#    usuario = request.user
#    if request.method == 'POST':
#        miformulario = UserEditForm(request.POST)
#        if miformulario.is_valid():
#            data = miformulario.cleaned_data
#            usuario.email = data['email']
#            usuario.password1 = data['password1']
#            usuario.password2 = data['password2']
#            usuario.save()

#            return render(request, 'app_coder/inicio.html',)
#    else:
#        miformulario = UserEditForm(initial={'email':usuario.email})
    
#    return render(request, 'app_coder/actualizar.html', {'miformulario':miformulario, 'usuario':usuario})
    
#def avatar(request):
#    if request.method == "POST":
#        comentario = Avatarform(request.POST, request.FILES)
#        if comentario.is_valid():
#            data = comentario.cleaned_data
#            avatares = Avatar.objects.filter(user=request.user)
#            if len(avatares) >=1:
#                avatares = Avatar.objects.get(user=request.user)
#                avatares.delete()
#            comentario_nuevo = Avatar(user=request.user, imagen=data['imagen'])
#            comentario_nuevo.save()
#        return render(request, "app_coder/inicio.html")
#    else:
#        miFormulario = Avatarform()
#        return render(request, "app_coder/avatar.html", {'formulario': miFormulario})   

class BlogsLista(ListView):
    template_name = 'app_coder/index.html'
    queryset = Comentario.objects.all().order_by('-fecha_creacion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #user = self.request.user
        #avatares = Avatar.objects.filter(id=user.id)
        context['avatar'] = Avatar.objects.all() #avatares[0].imagen.url
        return context

class BlogDetalle(DetailView):
    model = Comentario
    template_name = 'app_coder/detalle.html'

class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Comentario
    success_url = '/pages/'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']

class BlogDelete(DeleteView):
    model = Comentario
    success_url = '/pages/'


def about(request):
    return render(request, "app_coder/about.html")
