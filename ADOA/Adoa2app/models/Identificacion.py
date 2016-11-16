from django.db import models
from .Actividad import Actividad
from Adoa2app.validator.VacioValidator import VacioValidator

class Identificacion(Actividad):
    nombre = models.TextField()
    enunciado = models.TextField()
    
    def estaCompleto(self):
        validator = VacioValidator()
        
        if validator.validar(self.nombre) and validator.validar(self.enunciado):
            items = IdentificacionItem.objects.filter(Identificacion = self)
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
        identificacion = Identificacion()
        identificacion.nombre = self.nombre
        identificacion.enunciado = self.enunciado
        identificacion.ObjetoAprendizaje = oa
        identificacion.save()
        
        aItems = IdentificacionItem.objects.filter(identificacion = self)
        for item in aItems:
            itemClon = IdentificacionItem()
            itemClon.concepto = item.concepto
            itemClon.respuesta = item.respuesta
            itemClon.Identificacion = identificacion
            
            itemClon.save()
    
    class Meta:
        db_table = "Identificacion"
    
class IdentificacionItem(models.Model):
    concepto = models.TextField()
    respuesta = models.BooleanField()
    Identificacion = models.ForeignKey(Identificacion, on_delete=models.CASCADE)
    
    def estaCompleto(self):
        completo = True
        validator = VacioValidator()
        completo = completo and validator.validar(self.concepto)
        completo = completo and self.respuesta is not None
        
        return completo
    
    class Meta:
        db_table = "IdentificacionItem"