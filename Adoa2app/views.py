from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from Adoa2app.models.ObjetoAprendizaje import ObjetoAprendizaje
import json
from Adoa2app.models.PatronPedagogico import PatronPedagogico
from django.core import serializers

class Index(TemplateView):
    template_name = 'Index.html'
    
class LogOn(TemplateView):
    template_name = 'LogOn.html'
    
class CrearOA(TemplateView):
    model = ObjetoAprendizaje
    template_name = 'CrearOA.html'

    
def paso1(request):
    if request.method == 'POST':
        response_data = {}
        oatitulo = request.POST['titulo']
        oadescripcion = request.POST['descripcion']
        patron = request.POST['patron']
        oapatron = PatronPedagogico.objects.get(pk=patron)
        oa = ObjetoAprendizaje(titulo = oatitulo, descripcion = oadescripcion, patronPedagogico = oapatron)
        oa.save()

        response_data['result'] = 'Objeto creado!'
        response_data['oaid'] = oa.id

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def paso2(request):
    if request.method == 'POST':
        
        response_data = {}
        
        oaintroduccion = request.POST['introduccion']
        oaid = request.POST['oaid']
        
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        oa.introduccion = oaintroduccion
        oa.save()

        response_data['result'] = 'Objeto creado 2!'
        response_data['oaid'] = oa.id

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def traerPatrones(request):
    if request.method == 'POST':
        
        response_data = {}
        
        patrones = PatronPedagogico.objects.all()
        patronesJson = serializers.serialize('json', patrones)
        
        response_data['result'] = 'Patrones!'
        response_data['patrones'] = patronesJson

        return HttpResponse(
            patronesJson,
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def traerSeccionesPatron(request):
    if request.method == 'POST':
        
        response_data = {}
        
        patronId = request.POST['patron']
        patron = PatronPedagogico.objects.get(pk=patronId)
        secciones = patron.seccionnombre_set.all()
        
        seccionesJson = serializers.serialize('json', secciones)

        return HttpResponse(
            seccionesJson,
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        