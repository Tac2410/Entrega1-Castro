from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#class UsuarioFormulario(forms.Form):
#    nombre = forms.CharField(max_length=40)
#    password = forms.CharField(max_length=40)
#    email = forms.EmailField(max_length=254)

#class Buscar_usuario(forms.Form):
#    nombre = forms.CharField(max_length=40)

class Comentarioform(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(max_length=1000)
    imagen = forms.ImageField(allow_empty_file=True, required=False)

class FormcrearUsu(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_text = {k: '' for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_text = {k: '' for k in fields}

class Mensajeform(forms.Form):
    mensaje = forms.CharField(max_length=200)
    destinatario = forms.CharField(max_length=40)

class Avatarform(forms.Form):
    imagen = forms.ImageField()