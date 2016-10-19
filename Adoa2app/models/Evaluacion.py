from django.db import models

class Evaluacion(models.Model):
    enunciado = models.TextField()
    
    class Meta:
        db_table = "Evaluacion"
    
class EvaluacionItem(models.Model):
    pregunta = models.TextField()
    respuestaCorrecta = models.TextField()
    respuestaIncorrecta1 = models.TextField()
    respuestaIncorrecta2 = models.TextField()
    Evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table = "EvaluacionItem"