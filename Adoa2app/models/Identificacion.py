from django.db import models
from .Actividad import Actividad

class Identificacion(Actividad):
    enunciado = models.CharField(max_length=200)
    
    class Meta:
        db_table = "Identificacion"
    
class IdentificacionItem(models.Model):
    texto = models.CharField(max_length=200)
    respuesta = models.BooleanField()
    Identificacion = models.ForeignKey(Identificacion, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "IdentificacionItem"