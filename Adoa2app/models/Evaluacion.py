from django.db import models

class Evaluacion(models.Model):
    enunciado = models.CharField(max_length=200)
    
    class Meta:
        db_table = "Evaluacion"
    
class EvaluacionItem(models.Model):
    enunciado = models.CharField(max_length=200)
    respuestaCorrecta = models.CharField(max_length=200)
    respuestaIncorrecta1 = models.CharField(max_length=200)
    respuestaIncorrecta2 = models.CharField(max_length=200)
    Evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "EvaluacionItem"