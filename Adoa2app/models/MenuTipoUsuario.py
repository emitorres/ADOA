from django.db import models
from Adoa2app.usuario.managers import MenuTipoUsuarioManager
from .TipoUsuario import TipoUsuario
from .Menu import Menu

# Este modelo no era necesario, pero lo creo (accediendo a la tabla) para poder usar
# el matenimiento de accesos (y no solamente entrar por el menu a crear los accesos)
class MenuTipoUsuario(models.Model):
    
    menu        = models.ForeignKey(Menu)
    tipousuario = models.ForeignKey(TipoUsuario)

    objects = MenuTipoUsuarioManager() # Para usar managers

    class Meta:
        db_table = 'MenuTipoUsuario'
        ordering = ['tipousuario', 'menu']

