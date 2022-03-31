from django.db import models
from django.forms import CharField

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=40,primary_key=True)
    password = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)

class Administrador(models.Model):
    nombre = models.CharField(max_length=40,primary_key=True)
    password = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)

class Comentario(models.Model):
    titulo = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=1000)
    creador = models.CharField(max_length=40)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    auto_increment_id = models.AutoField(primary_key=True)
