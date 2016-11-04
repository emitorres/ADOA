from django.db import models
from .Actividad import Actividad

class Identificacion(Actividad):
    nombre = models.TextField()
    enunciado = models.TextField()
    
    class Meta:
        db_table = "Identificacion"
    
class IdentificacionItem(models.Model):
    concepto = models.TextField()
    respuesta = models.BooleanField()
    Identificacion = models.ForeignKey(Identificacion, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "IdentificacionItem"