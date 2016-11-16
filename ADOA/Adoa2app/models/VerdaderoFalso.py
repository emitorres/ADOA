from django.db import models
from .Actividad import Actividad
from Adoa2app.validator.VacioValidator import VacioValidator

class VerdaderoFalso(Actividad):
    nombre = models.TextField()
    enunciado = models.TextField()
    
    def estaCompleto(self):
        validator = VacioValidator()
        
        if validator.validar(self.nombre) and validator.validar(self.enunciado):
            items = VerdaderoFalsoItem.objects.filter(VerdaderoFalso = self)
            if items.count() > 0:
                for item in items:
                    if item.estaCompleto() is False:
                        return False       
            else:
                return False
        else:
            return False
        
        return True
    
    def clonar(self, oa):
        vof = VerdaderoFalso()
        vof.nombre = self.nombre
        vof.enunciado = self.enunciado
        vof.ObjetoAprendizaje = oa
        vof.save()
        
        aItems = VerdaderoFalsoItem.objects.filter(VerdaderoFalso = self)
        for item in aItems:
            itemClon = VerdaderoFalsoItem()
            itemClon.afirmacion = item.afirmacion
            itemClon.respuesta = item.respuesta
            itemClon.VerdaderoFalso = vof
            
            itemClon.save()
    
    class Meta:
        db_table = "VerdaderoFalso"
    
class VerdaderoFalsoItem(models.Model):
    afirmacion = models.TextField()
    respuesta = models.BooleanField()
    VerdaderoFalso = models.ForeignKey(VerdaderoFalso, on_delete=models.CASCADE)
    
    def estaCompleto(self):
        validator = VacioValidator()
        return validator.validar(self.afirmacion) and self.respuesta is not None

    class Meta:
        db_table = "VerdaderoFalsoItem"