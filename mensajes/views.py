from django.shortcuts import render
from mensajes.models import Mensajes
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from app_coder.forms import Mensajeform
from django.contrib.auth import get_user_model

# Create your views here.

#@login_required()
#def mensajes(request):
#    men = Mensajes.objects.filter(destinatario = request.user.username)
#    diccionario = {me}
#    return render(request, "mensajes/mensajes.html", diccionario)

class Mensajeslist(LoginRequiredMixin, ListView):
    template_name = 'mensajes/mensajes.html'
    def get_queryset(self):
        return Mensajes.objects.filter(destinatario=self.request.user.username).order_by('-fecha_creacion')

class MensajeDelete(DeleteView):
    model = Mensajes
    success_url = '/mensajes/'

class MensajeDetalle(DetailView):
    model = Mensajes
    template_name = 'mensajes/detalle_mensaje.html'

@login_required()
def enviar(request):
    if request.method == "POST":
        comentario = Mensajeform(request.POST)
        print(comentario.is_valid())
        if comentario.is_valid():
            User = get_user_model()
            data = comentario.cleaned_data
            envio = User.objects.filter(username=data['destinatario'])
            if len(envio) == 1:
                print(request.user.username)
                comentario_nuevo = Mensajes(data['mensaje'], envio[0], request.user.username)
                comentario_nuevo.save()
                return render(request, "app_coder/inicio.html")
            else:
                miFormulario = Mensajeform()
                return render(request, "mensajes/crear_mensaje.html", {'formulario': miFormulario, 'mensaje': 'Usuario Invalido'})
    else:
        miFormulario = Mensajeform()
        return render(request, "mensajes/crear_mensaje.html", {'formulario': miFormulario})