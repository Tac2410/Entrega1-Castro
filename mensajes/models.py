from django.db import models

# Create your models here.
class Mensajes (models.Model):
    mensaje = models.CharField(max_length=200)
    destinatario = models.CharField(max_length=40)
    creador = models.CharField(max_length=40)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ida = models.AutoField(primary_key=True, editable=False)