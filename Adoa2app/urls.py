from django.conf.urls import url

from . import views
from .views import Index
from .views import LogOn
from .views import CrearOA

urlpatterns = [
    url(r'^Index/$', Index.as_view()),
    url(r'^LogOn/$', LogOn.as_view()),
    url(r'^CrearOA/$', CrearOA.as_view()),
]