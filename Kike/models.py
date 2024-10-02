from django.db import models
from .enumeraciones import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

# MODELO SERIE
class Serie(models.Model):
    nombre=models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.nombre

# MODELO TILLA
class Tilla(models.Model):
    nombre=models.CharField(max_length=1000, null=False)
    serie=models.ForeignKey(Serie, on_delete=models.PROTECT)
    descripcion=models.TextField(max_length=5000, null=False)
    tp_producto=models.CharField(max_length=15, choices=GENERO, default='SIN ESPECIFICAR')
    precio=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(400000)])
    stock=models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    foto=models.ImageField(upload_to="tillas", null=True)

    def __str__(self):
        return self.nombre