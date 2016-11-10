from django.db import models
from .Actividad import Actividad
from Adoa2app.validator.VacioValidator import VacioValidator

class Ordenamiento(Actividad):
    nombre = models.TextField()
    enunciado = models.TextField()
    
    def estaCompleto(self):
        validator = VacioValidator()
        
        if validator.validar(self.nombre) and validator.validar(self.enunciado):
            items = OrdenamientoItem.objects.filter(Ordenamiento = self)
            if items.count() > 0:
                for item in items:
                    if item.estaCompleto() is False:
                        return False       
            else:
                return False
        else:
            return False
        
        return True
    
    class Meta:
        db_table = "Ordenamiento"
    
class OrdenamientoItem(models.Model):
    texto = models.TextField()
    orden = models.IntegerField()
    Ordenamiento = models.ForeignKey(Ordenamiento, on_delete=models.CASCADE)
    
    def estaCompleto(self):
        validator = VacioValidator()
        return validator.validar(self.texto) and validator.validarNumero(self.orden)
    
    class Meta:
        db_table = "OrdenamientoItem"