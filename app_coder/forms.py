from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=225)