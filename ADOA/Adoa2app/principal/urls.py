from django.conf.urls import patterns, include, url
from Adoa2app.principal.views import index, index_adoa, acercaDe

urlpatterns = patterns('',
   
   url(r'^$', index, name = 'index'),
   url(r'^acercaDe/$', acercaDe, name = 'acercaDe'),

   url(r'^adoa/', index_adoa, name = 'index_adoa'),
  

)
