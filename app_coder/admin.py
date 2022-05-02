from django.contrib import admin
from app_coder.models import Comentario
from mensajes.models import Mensajes
from accounts.models import Avatar

# Register your models here.
admin.site.register (Comentario)
admin.site.register (Avatar)
admin.site.register (Mensajes)