from django.db import models

# Create your models here.

class carros(models.Model):
    marca = models.CharField(blank=False, max_length=50)
    modelo = models.CharField(blank=False, max_length=50)
    color = models.CharField(blank=False, max_length=10)
    potencia = models.IntegerField()
    año = models.IntegerField()
    placa = models.CharField(blank=False, max_length=50)