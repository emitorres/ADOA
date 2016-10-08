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

urlpatterns = [
    url(r'^Index/$', Index.as_view()),
    url(r'^LogOn/$', LogOn.as_view()),
    url(r'^CrearOA/$', CrearOA.as_view()),
    url(r'^CrearOA/Paso1/$', Paso1),
    url(r'^CrearOA/Paso2/$', Paso2),
    url(r'^CrearOA/Paso3/$', Paso3),
    url(r'^CrearOA/TraerPatrones/$', TraerPatrones),
    url(r'^CrearOA/TraerSeccionesPatron/$', TraerSeccionesPatron),
]