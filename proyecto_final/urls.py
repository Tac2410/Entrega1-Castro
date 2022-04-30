"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from app_coder.views import * #inicio, crear_cuenta, administrador_iniciar_sesion, buscar_usuario, publicar, login_rec
from mensajes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='Inicio'),
    #path('administrador_iniciar_sesion/', administrador_iniciar_sesion, name="adminsesion"),
    #path('busqueda/', buscar_usuario, name="bucarusuario"),
    path('comentario/', publicar, name='publicar'),
    path('about/', about, name="about"),

    path('accounts/login/', login_rec, name='login'),
    path('accounts/signup/', crear_cuenta, name='register'),
    path('accounts/logout/', LogoutView.as_view(template_name="app_coder/mensajes.html"), name='logout'),
    path('accounts/profile/', actualizar_usuario, name='actualizarusu'),
    path('avatar/', avatar, name="avatar"),

    path('pages/', BlogsLista.as_view(), name="listablogs"),
    path('pages/<pk>/', BlogDetalle.as_view(), name='detalle'),
    path('pages/delete/<pk>/', BlogDelete.as_view(), name='delete'),
    path('pages/update/<pk>', BlogUpdate.as_view(), name='actualizar'),

    path('mensajes/', Mensajeslist.as_view(), name="listamensajes"),
    path('mensajes/<pk>', MensajeDetalle.as_view(), name="detallemensajes"),
    path('mensaje/delete/<pk>', MensajeDelete.as_view(), name="deletemensajes"),
    path('mensaje/crear/', enviar, name='enviar')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)