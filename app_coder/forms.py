from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=254)

class Buscar_usuario(forms.Form):
    nombre = forms.CharField(max_length=40)

class Comentarioform(forms.Form):
    titulo = forms.CharField(max_length=100)
    mensaje = forms.CharField(max_length=1000)
    creador = forms.CharField(max_length=40)