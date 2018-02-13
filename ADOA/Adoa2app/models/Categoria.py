# -*- coding: utf-8 -*-
from django.db import models

#from twisted.plugins.twisted_qtstub import errorMessage

# ------------ Modelo Usuario ------------
class Categoria(models.Model):#blank = false, null= false
    
    fotoUrl = models.CharField(max_length=45)
    categoria = models.CharField(max_length=100)
    
   

    def __unicode__(self):
        return u'%s - %s' % (self.fotoUrl)

    
    # La clase Meta interna es para especificar metadatos adicionales de un modelo
    class Meta:
        db_table = "Categoria"
       	ordering = ['categoria']

# ---------------------------------------------------------------------