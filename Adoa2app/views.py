from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from Adoa2app.models.ObjetoAprendizaje import ObjetoAprendizaje,\
    SeccionContenido
import json
from Adoa2app.models.PatronPedagogico import PatronPedagogico, SeccionNombre
from django.core import serializers
from Adoa2app.models import VerdaderoFalso, Identificacion
from Adoa2app.models.VerdaderoFalso import VerdaderoFalsoItem
from django.http.response import JsonResponse
from Adoa2app.models.Identificacion import IdentificacionItem

class Index(TemplateView):
    template_name = 'Index.html'
    
class LogOn(TemplateView):
    template_name = 'LogOn.html'
    
class CrearOA(TemplateView):
    model = ObjetoAprendizaje
    template_name = 'CrearOA.html'

    
def Paso1(request):
    if request.method == 'POST':
        response_data = {}
        oaid = int(request.POST['oaid'])
        if oaid==0:
            oatitulo = request.POST['titulo']
            oadescripcion = request.POST['descripcion']
            patron = request.POST['patron']
            oapatron = PatronPedagogico.objects.get(pk=patron)
            oa = ObjetoAprendizaje(titulo = oatitulo, descripcion = oadescripcion, PatronPedagogico = oapatron)
            oa.save()
            response_data['result'] = 'Objeto de Aprendizaje Creado!'
        else:
            oa = ObjetoAprendizaje.objects.get(pk=oaid)
            oa.titulo = request.POST['titulo']
            oa.descripcion = request.POST['descripcion']
            patron = request.POST['patron']
            oa.PatronPedagogico = PatronPedagogico.objects.get(pk=patron)
            oa.save()
            response_data['result'] = 'Objeto de Aprendizaje Editado!'
            
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
        
def Paso2(request):
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

def Paso3(request):
    if request.method == 'POST':
        
        response_data = {}
        
        oaid = request.POST['oaid']
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        
        secciones = json.loads(request.POST.get('secciones'))
        for seccion in secciones:
            seccionNombre = SeccionNombre.objects.get(pk=seccion['id'])
            seccionContenido = SeccionContenido(contenido = seccion['contenido'])
            seccionContenido.ObjetoAprendizaje = oa
            seccionContenido.SeccionNombre = seccionNombre
            seccionContenido.save()

        response_data['result'] = 'Secciones Guardadas!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def TraerPatrones(request):
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
        
def TraerSeccionesPatron(request):
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
        
def CrearVerdaderoFalso(request):
    if request.method == 'POST':
        
        response_data = {}
        
        oaid = request.POST['oaid']
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        
        verdaderoFalso = VerdaderoFalso(ObjetoAprendizaje = oa)
        verdaderoFalso.save()
        
        response_data['verdaderoFalsoId'] = verdaderoFalso.id
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def GuardarVerdaderoFalso(request):
    if request.method == 'POST':
        
        response_data = {}
        actividadId = request.POST['actividadId']
        verdaderoFalso = VerdaderoFalso.objects.get(pk=actividadId)
        verdaderoFalso.verdaderofalsoitem_set.all().delete()
        enunciado = request.POST['enunciado']
        
        terminos = json.loads(request.POST.get('terminos'))
        for termino in terminos:
            verdaderoFalsoItem = VerdaderoFalsoItem(afirmacion = termino['afirmacion'],respuesta = bool(int(termino['respuesta'])))
            verdaderoFalsoItem.VerdaderoFalso = verdaderoFalso
            verdaderoFalsoItem.save()
        
        verdaderoFalso.enunciado = enunciado
        verdaderoFalso.save()

        response_data['result'] = 'Verdadero o Falso Editado!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def TraerTerminosVerdaderoFalso(request):
    if request.method == 'POST':
        
        
        actividadId = request.POST['actividadId']
        verdaderoFalso = VerdaderoFalso.objects.get(pk=actividadId)
        
        terminos = verdaderoFalso.verdaderofalsoitem_set.all()
        
        terminosJson = serializers.serialize('json', terminos)

        return JsonResponse(
            {'enunciado':verdaderoFalso.enunciado,'terminos': terminosJson},
            content_type="application/json"
        )
    else:
        return JsonResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def CrearIdentificacion(request):
    if request.method == 'POST':
        
        response_data = {}
        
        oaid = request.POST['oaid']
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        
        identificacion = Identificacion(ObjetoAprendizaje = oa)
        identificacion.save()
        
        response_data['identificacionId'] = identificacion.id
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def GuardarIdentificacion(request):
    if request.method == 'POST':
        
        response_data = {}
        actividadId = request.POST['actividadId']
        identificacion = Identificacion.objects.get(pk=actividadId)
        identificacion.identificacionitem_set.all().delete()
        enunciado = request.POST['enunciado']
        
        terminos = json.loads(request.POST.get('terminos'))
        for termino in terminos:
            identificacionItem = IdentificacionItem(concepto = termino['concepto'],respuesta = bool(int(termino['respuesta'])))
            identificacionItem.Identificacion = identificacion
            identificacionItem.save()
        
        identificacion.enunciado = enunciado
        identificacion.save()

        response_data['result'] = 'Identificacion Editado!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def TraerTerminosIdentificacion(request):
    if request.method == 'POST':
        
        
        actividadId = request.POST['actividadId']
        identificacion = Identificacion.objects.get(pk=actividadId)
        
        terminos = identificacion.identificacionitem_set.all()
        
        terminosJson = serializers.serialize('json', terminos)

        return JsonResponse(
            {'enunciado':identificacion.enunciado,'terminos': terminosJson},
            content_type="application/json"
        )
    else:
        return JsonResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
        