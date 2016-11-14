'''
Created on 13 nov. 2016

@author: markos
'''

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible #para serializar en model

@deconstructible
class VacioValidator(object):
    def __init__(self, value=''):
        self.value = value
        
    def __eq__(self, other):
        return self.value == other.value
    
    #Metodo para usar como validador en un campo del modelo
    #Se considera vacio si la longitud es menor a 2    
    def __call__(self, value):
        if self.validar(value) is False:
            raise ValidationError(u'%s no se puede' % value)
        
        return True
    
    #Metodo para usar para validar normalmente un string
    def validar (self, value):
        if value is None or value == '' or len(value) < 2:
            return False
        
        return True
    
    #Metodo para validar un numero entero
    def validarNumero (self, value):
        if value is None or value < 0:
            return False
        
        return True