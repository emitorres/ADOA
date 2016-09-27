from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView

class Index(TemplateView):
    template_name = 'Index.html'
    
class LogOn(TemplateView):
    template_name = 'LogOn.html'
    
class CrearOA(TemplateView):
    template_name = 'CrearOA.html'