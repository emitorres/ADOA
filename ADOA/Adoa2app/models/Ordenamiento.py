from django.db import models
from .Actividad import Actividad

class Ordenamiento(Actividad):
    nombre = models.TextField()
    enunciado = models.TextField()
    
    class Meta:
        db_table = "Ordenamiento"
    
class OrdenamientoItem(models.Model):
    texto = models.TextField()
    orden = models.IntegerField()
    Ordenamiento = models.ForeignKey(Ordenamiento, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "OrdenamientoItem"