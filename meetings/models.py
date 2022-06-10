from datetime import datetime
from django.db import models
import pytz
from profiles.models import Perfil
from django.urls import reverse


class Ciudad(models.Model):
    ciudad      = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.ciudad

class Categoria(models.Model):
    categoria   = models.CharField(max_length=50)
        
    def __str__(self):
        return self.categoria

class Meeting(models.Model):
    titulo      = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    host        = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='host')
    publicado   = models.DateTimeField(auto_now_add=True)
    comienzo    = models.DateTimeField()
    cierre      = models.DateTimeField()
    asistentes  = models.ManyToManyField(Perfil, related_name='asistentes')
    ciudad      = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    direccion   = models.CharField(max_length=255)
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    en_curso    = models.BooleanField(default=False)
    culminado   = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-publicado']
    
    def __str__(self):
        return self.titulo
    
    # def get_absolute_url(self):
    #     return reverse('meetings:meeting-detail', kwargs={'pk': self.pk})
        

class Comentario(models.Model):
    meeting     = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    usuario     = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    comentario  = models.TextField()
    creado      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comentario

