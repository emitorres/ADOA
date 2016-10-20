from django.conf.urls import patterns, include, url
from Adoa2app.usuario.views import usuario_index,registro, iniciarSesion,perfil_index, perfil_editar,usuario_salir,usuario_acceso_denegado,informacion_registro, recuperar_contrasena, confirmar_cuenta,cambiar_clave

urlpatterns = patterns('',
    url(r'^index/$', usuario_index, name = 'usuario_index'),
    url(r'^registrarse/$', registro, name = 'usuario_registro'),
    url(r'^iniciar_sesion/$', iniciarSesion, name = 'usuario_iniciarSesion'),
	url(r'^perfil/$', perfil_index, name = 'perfil_index'),
	url(r'^perfil/editar/(\d+)/', perfil_editar, name = 'perfil_editar'),
	url(r'^salir/', usuario_salir, name = 'usuario_salir'),
	url(r'^acceso_denegado/$', usuario_acceso_denegado, name = 'usuario_acceso_denegado'),
	url(r'^informacion/$', informacion_registro, name = 'usuario_informacion_registro'),
	url(r'^recuperar_contrasena/$', recuperar_contrasena, name = 'usuario_recuperar_contrasena'),
	url(r'^confirmar_cuenta/([0-9A-Za-z_\-]+)/$',  confirmar_cuenta, name = 'usuario_confirmar_cuenta'),
	url(r'^cambiar_clave/(\d+)/', cambiar_clave, name = 'usuario_cambiar_clave'),
	#url(r'^confirmar_cuenta2/$',  confirmar_cuenta2, name = 'usuario_confirmar_cuenta'),







)
