from django.conf.urls import include, url
from . import views
from .views import Index
from .views import LogOn
from .views import CrearOA
from .views import paso1
from .views import paso2
from Adoa2app.views import traerPatrones

urlpatterns = [
    url(r'^Index/$', Index.as_view()),
    url(r'^LogOn/$', LogOn.as_view()),
    url(r'^CrearOA/$', CrearOA.as_view()),
    url(r'^CrearOA/paso1/$', paso1),
    url(r'^CrearOA/paso2/$', paso2),
    url(r'^CrearOA/traerPatrones/$', traerPatrones),
]