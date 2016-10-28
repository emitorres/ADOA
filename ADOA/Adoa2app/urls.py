from django.conf.urls import include, url
from . import views
from .views import Index
from .views import LogOn
from .views import CrearOA
from .views import Objetos
from .views import TraerObjetos
from .views import Paso1
from .views import Paso2
from .views import Paso3
from .views import TraerPatrones
from .views import TraerSeccionesPatron
from .views import CrearVerdaderoFalso
from .views import GuardarVerdaderoFalso
from .views import TraerTerminosVerdaderoFalso
from .views import CrearIdentificacion
from .views import GuardarIdentificacion
from .views import TraerTerminosIdentificacion
from .views import CrearOrdenamiento
from .views import GuardarOrdenamiento
from .views import TraerTerminosOrdenamiento
from .views import CrearAsociacion
from .views import GuardarAsociacion
from .views import TraerTerminosAsociacion
from .views import CrearVideo
from .views import GuardarVideo
from .views import TraerTerminosVideo
from .views import EliminarActividad
from .views import CrearPregunta
from .views import GuardarPregunta
from .views import TraerPregunta
from .views import EliminarPregunta
from .views import TraerDatosObjeto
from .views import TraerTerminosEvaluacion
from Adoa2app.views import EditarOA

urlpatterns = [
    url(r'^Index/$', Index.as_view()),
    url(r'^LogOn/$', LogOn.as_view()),
    url(r'^CrearOA/$', CrearOA, name = 'CrearOA'),
    #url(r'^CrearOA/$', CrearOA.as_view()),
    url(r'^EditarOA/(\d+)/$', EditarOA),
    url(r'^Objetos/$', Objetos, name= 'Objetos'),
    url(r'^Objetos/TraerObjetos/$', TraerObjetos),
    url(r'^CrearOA/Paso1/$', Paso1),
    url(r'^CrearOA/Paso2/$', Paso2),
    url(r'^CrearOA/Paso3/$', Paso3),
    url(r'^CrearOA/TraerPatrones/$', TraerPatrones),
    url(r'^CrearOA/TraerSeccionesPatron/$', TraerSeccionesPatron),
    url(r'^CrearOA/CrearVerdaderoFalso/$', CrearVerdaderoFalso),
    url(r'^CrearOA/GuardarVerdaderoFalso/$', GuardarVerdaderoFalso),
    url(r'^CrearOA/TraerTerminosVerdaderoFalso/$', TraerTerminosVerdaderoFalso),
    url(r'^CrearOA/CrearIdentificacion/$', CrearIdentificacion),
    url(r'^CrearOA/GuardarIdentificacion/$', GuardarIdentificacion),
    url(r'^CrearOA/TraerTerminosIdentificacion/$', TraerTerminosIdentificacion),
    url(r'^CrearOA/CrearOrdenamiento/$', CrearOrdenamiento),
    url(r'^CrearOA/GuardarOrdenamiento/$', GuardarOrdenamiento),
    url(r'^CrearOA/TraerTerminosOrdenamiento/$', TraerTerminosOrdenamiento),
    url(r'^CrearOA/CrearAsociacion/$', CrearAsociacion),
    url(r'^CrearOA/GuardarAsociacion/$', GuardarAsociacion),
    url(r'^CrearOA/TraerTerminosAsociacion/$', TraerTerminosAsociacion),
    url(r'^CrearOA/CrearVideo/$', CrearVideo),
    url(r'^CrearOA/GuardarVideo/$', GuardarVideo),
    url(r'^CrearOA/TraerTerminosVideo/$', TraerTerminosVideo),
    url(r'^CrearOA/EliminarActividad/$', EliminarActividad),
    url(r'^CrearOA/CrearPregunta/$', CrearPregunta),
    url(r'^CrearOA/GuardarPregunta/$', GuardarPregunta),
    url(r'^CrearOA/TraerPregunta/$', TraerPregunta),
    url(r'^CrearOA/EliminarPregunta/$', EliminarPregunta),
    url(r'^CrearOA/TraerDatosObjeto/$', TraerDatosObjeto),
    url(r'^CrearOA/TraerTerminosEvaluacion/$', TraerTerminosEvaluacion),
]