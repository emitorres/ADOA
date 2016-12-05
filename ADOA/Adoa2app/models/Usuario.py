# -*- coding: utf-8 -*-
from django.db import models
from .TipoUsuario import TipoUsuario
from Adoa2app.usuario.managers import UsuarioManager
from Adoa2app.validator.VacioValidator import VacioValidator
#from twisted.plugins.twisted_qtstub import errorMessage

# ------------ Modelo Usuario ------------
class Usuario(models.Model):#blank = false, null= false
    tipousuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, blank = True, null= True)
    nombre      = models.CharField(max_length=100, validators = [VacioValidator])
    apellido    = models.CharField(max_length=100, validators = [VacioValidator])
    dni         = models.CharField(max_length=15)
    carrera     = models.CharField(max_length=100)
    clave       = models.CharField(max_length=100)
    email       = models.EmailField(unique=True, error_messages={'unique' : 'El e-mail propocionado está en uso. <br> Por favor, ingrese uno diferente.'})
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