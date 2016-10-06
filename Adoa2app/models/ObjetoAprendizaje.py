from django.db import models
from .PatronPedagogico import PatronPedagogico
from .Evaluacion import Evaluacion
from .PatronPedagogico import SeccionNombre

class ObjetoAprendizaje(models.Model):
    titulo = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300)
    introduccion = models.CharField(max_length=2000)
    patronPedagogico = models.ForeignKey(PatronPedagogico, on_delete=models.CASCADE,null=True)
    evaluacion = models.OneToOneField(
        Evaluacion,
        on_delete=models.CASCADE,
        null=True
    )
    
    class Meta:
        db_table = "ObjetoAprendizaje"
    
class SeccionContenido(models.Model):
    contenido = models.CharField(max_length=2000)
    ObjetoAprendizaje = models.ForeignKey(ObjetoAprendizaje, on_delete=models.CASCADE)
    seccion = models.ForeignKey(SeccionNombre, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "SeccionContenido"