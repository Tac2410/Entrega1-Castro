from django.shortcuts import render
from app_coder.forms import UserEditForm, Avatarform, FormcrearUsu
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from accounts.models import Avatar

# Create your views here.

def crear_cuenta(request):
    if request.method == "POST":
        usuario = FormcrearUsu(request.POST)
        if usuario.is_valid():
            data = usuario.cleaned_data['username']
            usuario.save()
            return render(request, "app_coder/mensajes.html", {"mensaje": "Usuario Creado"})
        else:
            return render(request, "app_coder/mensajes.html", {"mensaje": "No paso la validacion"})
    else:
        miFormulario = FormcrearUsu()
        return render(request, "accounts/crearcuenta.html", {'formulario': miFormulario})

def login_rec(request):
    if request.method == "POST":
        usuario = AuthenticationForm(request, data=request.POST)
        if usuario.is_valid():
            usu = usuario.cleaned_data.get('username')
            con = usuario.cleaned_data.get('password')

            user = authenticate(username=usu, password=con)

            if user is not None:
                login(request, user)
                return render (request, "app_coder/mensajes.html", {"mensaje":f"Bienvenido {usu}"})
            else:
                return render (request, "app_coder/mensajes.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render (request, "app_coder/mensajes.html", {"mensaje":"Error, formulario erroneo"})
    else:
        miFormulario = AuthenticationForm()
        return render(request, "accounts/login.html", {'formulario': miFormulario})

@login_required()
def actualizar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        miformulario = UserEditForm(request.POST)
        if miformulario.is_valid():
            data = miformulario.cleaned_data
            usuario.email = data['email']
            usuario.password1 = data['password1']
            usuario.password2 = data['password2']
            usuario.save()

            return render(request, 'app_coder/inicio.html',)
    else:
        miformulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, 'accounts/actualizar.html', {'miformulario':miformulario, 'usuario':usuario})

def avatar(request):
    if request.method == "POST":
        comentario = Avatarform(request.POST, request.FILES)
        if comentario.is_valid():
            data = comentario.cleaned_data
            avatares = Avatar.objects.filter(user=request.user)
            if len(avatares) >=1:
                avatares = Avatar.objects.get(user=request.user)
                avatares.delete()
            comentario_nuevo = Avatar(user=request.user, imagen=data['imagen'])
            comentario_nuevo.save()
        return render(request, "app_coder/inicio.html")
    else:
        miFormulario = Avatarform()
        return render(request, "accounts/avatar.html", {'formulario': miFormulario}) 