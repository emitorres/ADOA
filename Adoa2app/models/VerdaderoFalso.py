from django.db import models
from .Actividad import Actividad

class VerdaderoFalso(Actividad):
    enunciado = models.TextField()
    
    class Meta:
        db_table = "VerdaderoFalso"
    
class VerdaderoFalsoItem(models.Model):
    afirmacion = models.TextField()
    respuesta = models.BooleanField()
    VerdaderoFalso = models.ForeignKey(VerdaderoFalso, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "VerdaderoFalsoItem"