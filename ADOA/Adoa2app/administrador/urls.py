from django.conf.urls import patterns, include, url
from Adoa2app.administrador.views import eliminar_acceso, index_administrador, usuarios_index, usuarios_edit, perfiles_edit, perfiles_index,menu_index, menu_edit,menu_tipo_index,menu_tipo_edit
urlpatterns = patterns('',
   
	url(r'^$', index_administrador, name = 'index_administrador'),  	
	url(r'^usuarios/$', usuarios_index, name = 'administrador_usuarios_index'), 
	url(r'^usuarios_edit/(\d+)/', usuarios_edit, name = 'administrador_usuarios_edit'), 
	url(r'^perfiles/', perfiles_index, name = 'administrador_perfiles_index'), 
	url(r'^perfiles_edit/(\d+)/', perfiles_edit, name = 'administrador_perfiles_edit'), 
	url(r'^menu/', menu_index, name = 'administrador_menu_index'), 
	url(r'^menu_edit/(\d+)/', menu_edit, name = 'administrador_menu_edit'), 
	url(r'^permisos/', menu_tipo_index, name = 'administrador_permisos_index'), 
	url(r'^permisos_edit/(\d+)/', menu_tipo_edit, name = 'administrador_menu_tipo_edit'), 
	url(r'^eliminar_acceso/(\d+)/', eliminar_acceso, name = 'administrador_eliminar_acceso'), 

)
