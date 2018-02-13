# -*- coding: utf-8 -*-
from django.db import models
from .PatronPedagogico import PatronPedagogico
from .PatronPedagogico import SeccionNombre
from .Usuario import Usuario
from .Categoria import Categoria
from Adoa2app.validator.VacioValidator import VacioValidator

class ObjetoAprendizaje(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    introduccion = models.TextField()
    PatronPedagogico = models.ForeignKey(PatronPedagogico, on_delete=models.CASCADE,null=True)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, default = 1)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, default = 1)

    def estaCompleto (self):
        from .Evaluacion import Evaluacion
        validator = VacioValidator()
        incompleto = []
        if validator.validar(self.titulo) and \
           validator.validar(self.descripcion):
           
            if validator.validar(self.introduccion) is False:
                incompleto.append('Introducción')
            
            evaluacion = Evaluacion.objects.get(ObjetoAprendizaje = self)   
            if evaluacion.estaCompleto() is False:
                incompleto.append('Evaluación')
            
            items = SeccionContenido.objects.filter(ObjetoAprendizaje = self)
            if items.count() > 0:
                contenidoIncompleto = False
                listado = list(items)
                i = 0
                while contenidoIncompleto is False and items.count() > i:
                    item = listado[i]
                    if item.estaCompleto() is False:
                        contenidoIncompleto = True
                        incompleto.append('Contenido')
                    i+=1
            else:
                incompleto.append('Contenido')
        else:
            incompleto.append('Información')
        
        return (len(incompleto) == 0, incompleto) 
        
    class Meta:
        db_table = "ObjetoAprendizaje"
    
class SeccionContenido(models.Model):
    contenido = models.TextField()
    ObjetoAprendizaje = models.ForeignKey(ObjetoAprendizaje, on_delete=models.CASCADE)
    SeccionNombre = models.ForeignKey(SeccionNombre, on_delete=models.CASCADE)
    
    #Informa si el objeto esta completo
    def estaCompleto(self):
        validator = VacioValidator()
        return validator.validar(self.contenido)
    
    class Meta:
        db_table = "SeccionContenido"