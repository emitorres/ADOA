from django.conf.urls import patterns, include, url
from Adoa2app.usuario.views import usuario_index,registro, iniciarSesion,perfil_index, perfil_editar,usuario_salir,usuario_acceso_denegado,informacion_registro, recuperar_contrasena, confirmar_cuenta,cambiar_clave,cambio_clave,eliminar_usuario,index_usuarioBase

urlpatterns = patterns('',
 	url(r'^configuracion/$', index_usuarioBase, name = 'index_usuarioBase'),
    url(r'^index/$', usuario_index, name = 'usuario_index'),
    url(r'^registrarse/$', registro, name = 'usuario_registro'),
    url(r'^iniciar_sesion/$', iniciarSesion, name = 'usuario_iniciarSesion'),
	url(r'^configuracion/perfil/$', perfil_index, name = 'perfil_index'),
	url(r'^configuracion/perfil/editar/(\d+)/', perfil_editar, name = 'perfil_editar'),
	url(r'^salir/', usuario_salir, name = 'usuario_salir'),
	url(r'^acceso_denegado/$', usuario_acceso_denegado, name = 'usuario_acceso_denegado'),
	url(r'^informacion/$', informacion_registro, name = 'usuario_informacion_registro'),
	url(r'^recuperar_contrasena/$', recuperar_contrasena, name = 'usuario_recuperar_contrasena'),
	url(r'^confirmar_cuenta/([0-9A-Za-z_\-]+)/$',  confirmar_cuenta, name = 'usuario_confirmar_cuenta'),
	url(r'^recuperar/cambio_clave/([0-9A-Za-z_\-]+)/$', cambiar_clave, name = 'usuario_cambiar_clave'),
	url(r'^configuracion/cambio_clave/(\d+)/', cambio_clave, name = 'usuario_cambio_clave'),
	url(r'^usuarios_delete/(\d+)/', eliminar_usuario, name='usuario_eliminar_usuario'),
	#url(r'^confirmar_cuenta2/$',  confirmar_cuenta2, name = 'usuario_confirmar_cuenta'),







)
