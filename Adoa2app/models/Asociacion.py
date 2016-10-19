from django.db import models
from .Actividad import Actividad

class Asociacion(Actividad):
    enunciado = models.TextField()
    
    class Meta:
        db_table = "Asociacion"
    
class AsociacionItem(models.Model):
    campo1 = models.TextField()
    campo2 = models.TextField()
    Asociacion = models.ForeignKey(Asociacion, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "AsociacionItem"