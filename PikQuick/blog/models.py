# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

#published_in = models.ForeignKey(Entrada)
# Create your models here.
class Entrada(models.Model):
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Todas las Entradas"
        ordering = ['-fecha']

    titulo = models.CharField(u'Título', max_length = 100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    img1 = models.FileField(u'Imagen de portada',upload_to = 'img_public', default='null')
    img2 = models.FileField(u'Imagen de portada',upload_to = 'img_public', default='null')
    published = models.BooleanField(u'Publicado?', default=True)
    #autor = models.ForeignKey(User)
    #categoria = models.ManyToManyField('Categoria')
    #resumen= models.CharField(u'Resumen',max_length=512)
    #contenido = models.TextField(u'Contenido')

    def __str__(self):
        return self.titulo
