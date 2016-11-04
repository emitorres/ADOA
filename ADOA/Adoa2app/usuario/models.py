from django.db import models
from django.core.exceptions import ValidationError
from Adoa2app.usuario.managers import TipoUsuarioManager, UsuarioManager, MenuManager, MenuTipoUsuarioManager
from passlib.hash import pbkdf2_sha256

# ------------ Modelo Tipo Usuario ------------
            
class TipoUsuario(models.Model):

    def validate_vacio_nulo(valor):
        if (valor == '') or (valor == None) or (len(valor) < 3):
            raise ValidationError(u'%s no se puede' % valor)

    nombre     = models.CharField(max_length=100, validators = [validate_vacio_nulo])
    created    = models.DateTimeField(auto_now_add = True) # Usar datetime.date.today() - import datetime
    updated    = models.DateTimeField(auto_now = True)

    objects = TipoUsuarioManager() # Para usar managers

    def __unicode__(self):
        return u'%s' % (self.nombre)
       
    class Meta:
        db_table = "TipoUsuario"

# ---------------------------------------------------------------------


# ------------ Modelo Usuario ------------

class Usuario(models.Model):#blank = false, null= false

    def validate_vacio_nulo(valor):
        if (valor == '') or (valor == None) or (len(valor) < 3):
            raise ValidationError(u'%s no se puede' % valor)

    tipousuario = models.ForeignKey(TipoUsuario,blank = True, null= True)
    nombre      = models.CharField(max_length=100 ,validators = [validate_vacio_nulo])
    apellido    = models.CharField(max_length=100)
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
class token(models.Model):
    token = models.CharField(max_length = 50,blank = True, null= True)
    usuario = models.ForeignKey(Usuario,blank = True, null= True)

    def __unicode__(self):
        return u'%s - %s' % (self.token)

# ------------ Modelo Menu ------------

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

# ---------------------------------------------------------------------

# ------------ Modelo Menu Usuario Tipo ------------
# Este modelo no era necesario, pero lo creo (accediendo a la tabla) para poder usar
# el matenimiento de accesos (y no solamente entrar por el menu a crear los accesos)

class MenuTipoUsuario(models.Model):
    
    menu        = models.ForeignKey(Menu)
    tipousuario = models.ForeignKey(TipoUsuario)

    objects = MenuTipoUsuarioManager() # Para usar managers

    class Meta:
        #db_table = 'Menu_tipousuarios'
        ordering = ['tipousuario', 'menu']