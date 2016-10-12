from django.conf.urls import include, url
from . import views
from .views import Index
from .views import LogOn
from .views import CrearOA
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

urlpatterns = [
    url(r'^Index/$', Index.as_view()),
    url(r'^LogOn/$', LogOn.as_view()),
    url(r'^CrearOA/$', CrearOA.as_view()),
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
]