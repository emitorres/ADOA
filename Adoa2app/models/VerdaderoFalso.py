from django.db import models
from .Actividad import Actividad

class VerdaderoFalso(Actividad):
    enunciado = models.CharField(max_length=200)
    
    class Meta:
        db_table = "VerdaderoFalso"
    
class VerdaderoFalsoItem(models.Model):
    afirmacion = models.CharField(max_length=200)
    respuesta = models.BooleanField()
    VerdaderoFalso = models.ForeignKey(VerdaderoFalso, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "VerdaderoFalsoItem"