from django.db import models
from .Actividad import Actividad

class Video(Actividad):
    descripcion = models.CharField(max_length=200)
    link = models.CharField(max_length=300)
    
    class Meta:
        db_table = "Video"