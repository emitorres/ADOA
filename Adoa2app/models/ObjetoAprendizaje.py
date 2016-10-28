from django.db import models
from .PatronPedagogico import PatronPedagogico
from .Evaluacion import Evaluacion
from .PatronPedagogico import SeccionNombre

class ObjetoAprendizaje(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    introduccion = models.TextField()
    PatronPedagogico = models.ForeignKey(PatronPedagogico, on_delete=models.CASCADE,null=True)
    Evaluacion = models.OneToOneField(
        Evaluacion,
        on_delete=models.CASCADE,
        null=True
    )
    
    class Meta:
        db_table = "ObjetoAprendizaje"
    
class SeccionContenido(models.Model):
    contenido = models.TextField()
    ObjetoAprendizaje = models.ForeignKey(ObjetoAprendizaje, on_delete=models.CASCADE)
    SeccionNombre = models.ForeignKey(SeccionNombre, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "SeccionContenido"