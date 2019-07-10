# Create your models here.
from django.db import models


class Gestor(models.Model):
    nombre = models.CharField(max_length=200)

class ComunidadEnergetica(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField()
    latitud = models.FloatField()
    longitud=models.FloatField()
    id_gestor = models.IntegerField(null=True)

class InscritoComunidad(models.Model):
    dni = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200, null=True)
    latitud_der = models.FloatField()
    longitud_der = models.FloatField()
    nombre_der= models.CharField(max_length=200)
    id_comunidad = models.IntegerField()






