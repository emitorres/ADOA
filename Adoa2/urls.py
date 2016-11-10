from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Adoa2app.urls')),
    #url(r'^', include('Adoa2app.urls')),
    url(r'^administrador/', include('Adoa2app.administrador.urls', namespace = 'administrador')),
    url(r'^usuario/', include('Adoa2app.usuario.urls', namespace = 'usuario')),
    url(r'^', include('Adoa2app.principal.urls', namespace = 'principal')),
    url(r'^adoa/', include('Adoa2app.principal.urls', namespace = 'principal_adoa')),
)