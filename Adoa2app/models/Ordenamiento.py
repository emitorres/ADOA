from django.db import models
from .Actividad import Actividad

class Ordenamiento(Actividad):
    enunciado = models.CharField(max_length=200)
    
    class Meta:
        db_table = "Ordenamiento"
    
class OrdenamientoItem(models.Model):
    texto = models.CharField(max_length=200)
    orden = models.IntegerField()
    Ordenamiento = models.ForeignKey(Ordenamiento, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "OrdenamientoItem"