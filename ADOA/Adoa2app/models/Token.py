'''
Created on 13 nov. 2016

@author: markos
'''
from django.db import models
from .Usuario import Usuario

class Token(models.Model):
    token = models.CharField(max_length = 50,blank = True, null= True)
    usuario = models.ForeignKey(Usuario,blank = True, null= True)

    def __unicode__(self):
        return u'%s - %s' % (self.token)
       
    class Meta:
        db_table = "Token"