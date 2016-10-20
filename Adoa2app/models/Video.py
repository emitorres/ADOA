from django.db import models
from .Actividad import Actividad

class Video(Actividad):
    descripcion = models.TextField()
    link = models.CharField(max_length=300)
    
    class Meta:
        db_table = "Video"