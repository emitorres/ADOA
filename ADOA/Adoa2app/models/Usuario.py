from django.db import models
from .TipoUsuario import TipoUsuario
from Adoa2app.usuario.managers import UsuarioManager
from Adoa2app.validator.VacioValidator import VacioValidator

# ------------ Modelo Usuario ------------
class Usuario(models.Model):#blank = false, null= false
    tipousuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, blank = True, null= True)
    nombre      = models.CharField(max_length=100, validators = [VacioValidator])
    apellido    = models.CharField(max_length=100, validators = [VacioValidator])
    dni         = models.CharField(max_length=15)
    carrera     = models.CharField(max_length=100)
    clave       = models.CharField(max_length=100)
    email       = models.EmailField()
    estado      = models.BooleanField()
    created     = models.DateTimeField(auto_now_add = True) # Usar datetime.date.today() - import datetime
    updated     = models.DateTimeField(auto_now = True)
    sexo        = models.BooleanField()
    
    objects = UsuarioManager() # Para usar managers

    def __unicode__(self):
        return u'%s - %s' % (self.nombre)

    
    # La clase Meta interna es para especificar metadatos adicionales de un modelo
    class Meta:
        db_table = "Usuario"
        ordering = ['tipousuario', 'nombre']

# ---------------------------------------------------------------------