from django.db import models
from .ObjetoAprendizaje import ObjetoAprendizaje
from Adoa2app.validator.VacioValidator import VacioValidator

class Evaluacion(models.Model):
    enunciado = models.TextField() 
    ObjetoAprendizaje = models.OneToOneField(ObjetoAprendizaje, on_delete=models.CASCADE, null=False, default=1)
    
    def estaCompleto(self):
        #validator = VacioValidator()
        #if validator.validar(self.enunciado): #No se completa nunca este campo 
        items = EvaluacionItem.objects.filter(Evaluacion = self)
        if items.count() > 0:
            for item in items:
                if item.estaCompleto() is False:
                    return False
        #    else:
        #        return False
        else:
            return False
        
        return True
    
    class Meta:
        db_table = "Evaluacion"
        

class EvaluacionItem(models.Model):
    pregunta = models.TextField()
    respuestaCorrecta = models.TextField()
    respuestaIncorrecta1 = models.TextField()
    respuestaIncorrecta2 = models.TextField()
    ordenRespuestaCorrecta = models.IntegerField()
    ordenRespuestaIncorrecta1 = models.IntegerField()
    ordenRespuestaIncorrecta2 = models.IntegerField()
    Evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE,null=True)

    def estaCompleto(self):
        validator = VacioValidator()
        
        if validator.validar(self.pregunta) is False \
           or validator.validar(self.respuestaCorrecta) is False \
           or validator.validar(self.respuestaIncorrecta1) is False \
           or validator.validar(self.respuestaIncorrecta2) is False \
           or validator.validarNumero(self.ordenRespuestaCorrecta) is False \
           or validator.validarNumero(self.ordenRespuestaIncorrecta1) is False \
           or validator.validarNumero(self.ordenRespuestaIncorrecta2) is False:
            return False
        
        return True
    
    
    class Meta:
        db_table = "EvaluacionItem"