from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Create your models here.

class Comentario(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1000)
    creador = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='blogs', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)
    def __str__(self):
        return f"Titulo: {self.titulo} - Creador: {self.creador} - Fecha de creacion: {self.fecha_creacion}"

#class Avatar (models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
#    id = models.AutoField(primary_key=True, editable=False)