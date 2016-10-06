from django.db import models
from .Actividad import Actividad

class Asociacion(Actividad):
    enunciado = models.CharField(max_length=200)
    
    class Meta:
        db_table = "Asociacion"
    
class AsociacionItem(models.Model):
    campo1 = models.CharField(max_length=200)
    campo2 = models.CharField(max_length=200)
    asociacion = models.ForeignKey(Asociacion, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "AsociacionItem"