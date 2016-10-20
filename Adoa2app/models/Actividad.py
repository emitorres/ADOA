from django.db import models
from .ObjetoAprendizaje import ObjetoAprendizaje

class Actividad(models.Model):
    ObjetoAprendizaje = models.ForeignKey(ObjetoAprendizaje, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Actividad"