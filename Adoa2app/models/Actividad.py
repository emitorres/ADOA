from django.db import models
from .ObjetoAprendizaje import ObjetoAprendizaje

class Actividad(models.Model):
    ObjetoAprendizaje = models.ForeignKey(ObjetoAprendizaje, on_delete=models.CASCADE)
    
    def getAll(self):
        from .Ordenamiento import Ordenamiento
        from .Asociacion import Asociacion
        from .Identificacion import Identificacion
        from .VerdaderoFalso import VerdaderoFalso
        from .Video import Video

        listaActividades = []
        listaActividades.append(Asociacion.objects.filter(ObjetoAprendizaje = self.ObjetoAprendizaje))
        listaActividades.append(Identificacion.objects.filter(ObjetoAprendizaje = self.ObjetoAprendizaje))
        listaActividades.append(VerdaderoFalso.objects.filter(ObjetoAprendizaje = self.ObjetoAprendizaje))
        listaActividades.append(Video.objects.filter(ObjetoAprendizaje = self.ObjetoAprendizaje))
        listaActividades.append(Ordenamiento.objects.filter(ObjetoAprendizaje = self.ObjetoAprendizaje))
        
        return listaActividades
            
        
    class Meta:
        db_table = "Actividad"