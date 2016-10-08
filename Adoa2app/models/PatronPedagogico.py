from django.db import models

class PatronPedagogico(models.Model):
    ACTIVIDADES = (
        ('1', 'VerdaderoFalso'),
        ('2', 'Asociacion'),
        ('3', 'Video'),
        ('4', 'Ordenamiento'),
        ('5', 'Identificacion'),
    )
    nombre = models.CharField(max_length=100)
    ActividadSugerida = models.CharField(max_length=2, choices=ACTIVIDADES)
    
    class Meta:
        db_table = "PatronPedagogico"
    
class SeccionNombre(models.Model):
    nombre = models.CharField(max_length=100)
    PatronPedagogico = models.ForeignKey(PatronPedagogico, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "SeccionNombre"