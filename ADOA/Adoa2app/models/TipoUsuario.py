from django.db import models
from Adoa2app.usuario.managers import TipoUsuarioManager
from Adoa2app.validator.VacioValidator import VacioValidator

# ------------ Modelo Tipo Usuario ------------
class TipoUsuario(models.Model):
    nombre     = models.CharField(max_length=100, validators = [VacioValidator])
    created    = models.DateTimeField(auto_now_add = True) # Usar datetime.date.today() - import datetime
    updated    = models.DateTimeField(auto_now = True)

    objects = TipoUsuarioManager() # Para usar managers

    def __unicode__(self):
        return u'%s' % (self.nombre)
       
    class Meta:
        db_table = "TipoUsuario"

# ---------------------------------------------------------------------