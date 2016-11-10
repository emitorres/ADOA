from django.db import models
from .Actividad import Actividad
from Adoa2app.validator.VacioValidator import VacioValidator

class Video(Actividad):
    nombre = models.TextField()
    descripcion = models.TextField()
    link = models.CharField(max_length=300)
    
    def estaCompleto(self):
        validator = VacioValidator()
        if validator.validar(self.nombre) is False \
           or validator.validar(self.descripcion) is False \
           or validator.validar(self.link) is False:
            return False
        
        return True
    
    class Meta:
        db_table = "Video"