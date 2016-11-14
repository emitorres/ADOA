'''
Created on 13 nov. 2016

@author: markos
'''
from django.db import models
from Adoa2app.usuario.managers import MenuManager
from .TipoUsuario import TipoUsuario

class Menu(models.Model):
    nombre     = models.CharField(max_length=100)
    url        = models.CharField(max_length=100, blank=True, null=True)
    created    = models.DateTimeField(auto_now_add = True) # Usar datetime.date.today() - import datetime
    updated    = models.DateTimeField(auto_now = True)
    tipousuarios = models.ManyToManyField(TipoUsuario, blank=True, null=True)

    objects = MenuManager() # Para usar managers

    def __unicode__(self):
        return u'%s' % (self.nombre)

    # La clase Meta interna es para especificar metadatos adicionales de un modelo
    class Meta:
        db_table = 'Menu'
        ordering = ['nombre']