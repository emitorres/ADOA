from django.db import models
from .Actividad import Actividad
from Adoa2app.validator.VacioValidator import VacioValidator

class Asociacion(Actividad):
    nombre = models.TextField()
    enunciado = models.TextField()
    
    def estaCompleto(self):
        validator = VacioValidator()
        
        if validator.validar(self.nombre) and validator.validar(self.enunciado):
            items = AsociacionItem.objects.filter(Asociacion = self)
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
        asociacion = Asociacion()
        asociacion.nombre = self.nombre
        asociacion.enunciado = self.enunciado
        asociacion.ObjetoAprendizaje = oa
        asociacion.save()
        
        aItems = AsociacionItem.objects.filter(Asociacion = self)
        for item in aItems:
            itemClon = AsociacionItem()
            itemClon.campo1 = item.campo1
            itemClon.campo2 = item.campo2
            itemClon.ordenCampo1 = item.ordenCampo1
            itemClon.ordenCampo2 = item.ordenCampo2
            itemClon.Asociacion = asociacion
            
            itemClon.save()
        
    
    class Meta:
        db_table = "Asociacion"
    
class AsociacionItem(models.Model):
    ordenCampo1 = models.IntegerField()
    campo1 = models.TextField()
    ordenCampo2 = models.IntegerField()
    campo2 = models.TextField()
    Asociacion = models.ForeignKey(Asociacion, on_delete=models.CASCADE)
    
    def estaCompleto(self):
        validator = VacioValidator()
        return validator.validar(self.campo1) and validator.validar(self.campo2)
    
    class Meta:
        db_table = "AsociacionItem"