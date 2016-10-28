from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from Adoa2app.models.ObjetoAprendizaje import ObjetoAprendizaje,\
    SeccionContenido
import json
from Adoa2app.models.PatronPedagogico import PatronPedagogico, SeccionNombre
from django.core import serializers
from Adoa2app.models import VerdaderoFalso, Identificacion, Ordenamiento,\
    Asociacion, Video, Actividad, Evaluacion
from Adoa2app.models.VerdaderoFalso import VerdaderoFalsoItem
from django.http.response import JsonResponse, Http404
from Adoa2app.models.Identificacion import IdentificacionItem
from Adoa2app.models.Ordenamiento import OrdenamientoItem
from Adoa2app.models.Asociacion import AsociacionItem
from Adoa2app.models.Evaluacion import EvaluacionItem
from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from Adoa2app.usuario.models import Usuario

class Index(TemplateView):
    template_name = 'Index.html'
    
class LogOn(TemplateView):
    template_name = 'LogOn.html'
    
def CrearOA(request):
    model = ObjetoAprendizaje
    template_name = 'CrearOA.html'

    id = request.session['usuario'].id
    usuario = Usuario.objects.get(id= id)
    
    return render_to_response(template_name, locals(), context_instance = RequestContext(request))  
"""
def CrearOA(request):

    id = request.session['usuario'].id
    usuario = Usuario.objects.get(id= id)

    return render_to_response('CrearOA.html', locals(), context_instance = RequestContext(request))  
"""
def EditarOA(request, objId):
    try:
        objeto = ObjetoAprendizaje.objects.get(pk=objId)
    except ObjetoAprendizaje.DoesNotExist:
        raise Http404("Poll does not exist")
    id = request.session['usuario'].id
    usuario = Usuario.objects.get(id= id)
    return render(request, 'CrearOA.html', {'id': id, 'objeto': objeto})

def Objetos(request):
    model = ObjetoAprendizaje
    template_name = 'Objetos.html'
    
    id = request.session['usuario'].id
    usuario = Usuario.objects.get(id= id)
    return render_to_response(template_name, locals(), context_instance = RequestContext(request))  

    
def Paso1(request):
    if request.method == 'POST':
        response_data = {}
        oaid = int(request.POST['oaid'])
        if oaid==0:
            oatitulo = request.POST['titulo']
            oadescripcion = request.POST['descripcion']
            patron = request.POST['patron']
            oapatron = PatronPedagogico.objects.get(pk=patron)
            evaluacion = Evaluacion()
            evaluacion.save()
            oa = ObjetoAprendizaje(titulo = oatitulo, descripcion = oadescripcion, PatronPedagogico = oapatron, Evaluacion = evaluacion)
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
            
        response_data['evaluacionid'] = oa.Evaluacion.id
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
        
        patrones = PatronPedagogico.objects.all()
        patronesJson = serializers.serialize('json', patrones)

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
        
def CrearOrdenamiento(request):
    if request.method == 'POST':
        
        response_data = {}
        
        oaid = request.POST['oaid']
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        
        ordenamiento = Ordenamiento(ObjetoAprendizaje = oa)
        ordenamiento.save()
        
        response_data['ordenamientoId'] = ordenamiento.id
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def GuardarOrdenamiento(request):
    if request.method == 'POST':
        
        response_data = {}
        actividadId = request.POST['actividadId']
        ordenamiento = Ordenamiento.objects.get(pk=actividadId)
        ordenamiento.ordenamientoitem_set.all().delete()
        enunciado = request.POST['enunciado']
        
        terminos = json.loads(request.POST.get('terminos'))
        for termino in terminos:
            ordenamientoItem = OrdenamientoItem(texto = termino['texto'],orden = termino['orden'])
            ordenamientoItem.Ordenamiento = ordenamiento
            ordenamientoItem.save()
        
        ordenamiento.enunciado = enunciado
        ordenamiento.save()

        response_data['result'] = 'Ordenamiento Editado!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def TraerTerminosOrdenamiento(request):
    if request.method == 'POST':
        
        
        actividadId = request.POST['actividadId']
        ordenamiento = Ordenamiento.objects.get(pk=actividadId)
        
        terminos = ordenamiento.ordenamientoitem_set.all()
        
        terminosJson = serializers.serialize('json', terminos)

        return JsonResponse(
            {'enunciado':ordenamiento.enunciado,'terminos': terminosJson},
            content_type="application/json"
        )
    else:
        return JsonResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def CrearAsociacion(request):
    if request.method == 'POST':
        
        response_data = {}
        
        oaid = request.POST['oaid']
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        
        asociacion = Asociacion(ObjetoAprendizaje = oa)
        asociacion.save()
        
        response_data['asociacionId'] = asociacion.id
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def GuardarAsociacion(request):
    if request.method == 'POST':
        
        response_data = {}
        actividadId = request.POST['actividadId']
        asociacion = Asociacion.objects.get(pk=actividadId)
        asociacion.asociacionitem_set.all().delete()
        enunciado = request.POST['enunciado']
        
        terminos = json.loads(request.POST.get('terminos'))
        for termino in terminos:
            asociacionItem = AsociacionItem(campo1 = termino['campo1'],campo2 = termino['campo2'])
            asociacionItem.Asociacion = asociacion
            asociacionItem.save()
        
        asociacion.enunciado = enunciado
        asociacion.save()

        response_data['result'] = 'Asociacion Editado!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def TraerTerminosAsociacion(request):
    if request.method == 'POST':
        
        
        actividadId = request.POST['actividadId']
        asociacion = Asociacion.objects.get(pk=actividadId)
        
        terminos = asociacion.asociacionitem_set.all()
        
        terminosJson = serializers.serialize('json', terminos)

        return JsonResponse(
            {'enunciado':asociacion.enunciado,'terminos': terminosJson},
            content_type="application/json"
        )
    else:
        return JsonResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def CrearVideo(request):
    if request.method == 'POST':
        
        response_data = {}
        
        oaid = request.POST['oaid']
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        
        video = Video(ObjetoAprendizaje = oa)
        video.save()
        
        response_data['videoId'] = video.id
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def GuardarVideo(request):
    if request.method == 'POST':
        
        response_data = {}
        actividadId = request.POST['actividadId']
        video = Video.objects.get(pk=actividadId)
        
        descripcion = request.POST['descripcion']
        link = request.POST['link']
        
        video.descripcion = descripcion
        video.link = link
        video.save()

        response_data['result'] = 'Video Editado!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def TraerTerminosVideo(request):
    if request.method == 'POST':
        
        actividadId = request.POST['actividadId']
        video = Video.objects.get(pk=actividadId)


        return JsonResponse(
            {'descripcion':video.descripcion,'link': video.link},
            content_type="application/json"
        )
    else:
        return JsonResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def EliminarActividad(request):
    if request.method == 'POST':
        
        response_data = {}
        
        actividadId = request.POST['actividadId']
        actividad = Actividad.objects.get(pk=actividadId)
        actividad.delete()

        response_data['result'] = 'Actividad Eliminada!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def TraerObjetos(request):
    if request.method == 'POST':
        
        response_data = {}
        
        objetos = ObjetoAprendizaje.objects.all()
        objetosJson = serializers.serialize('json', objetos)
        
        response_data['result'] = 'Objetos!'
        response_data['objetos'] = objetosJson

        return HttpResponse(
            objetosJson,
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def CrearPregunta(request):
    if request.method == 'POST':
        
        response_data = {}
        evaluacionId = request.POST['evaluacionId']
        evaluacion = Evaluacion.objects.get(pk=evaluacionId)
        
        pregunta = request.POST['pregunta']
        respuestacorrecta = request.POST['respuestacorrecta']
        respuestaincorrecta1 = request.POST['respuestaincorrecta1']
        respuestaincorrecta2 = request.POST['respuestaincorrecta2']
        ordenrespuestacorrecta = request.POST['ordenrespuestacorrecta']
        ordenrespuestaincorrecta1 = request.POST['ordenrespuestaincorrecta1']
        ordenrespuestaincorrecta2 = request.POST['ordenrespuestaincorrecta2']
        
        evaluacionItem = EvaluacionItem(pregunta = pregunta, respuestaCorrecta = respuestacorrecta, respuestaIncorrecta1 = respuestaincorrecta1, respuestaIncorrecta2 = respuestaincorrecta2,
                                        ordenRespuestaCorrecta = ordenrespuestacorrecta, ordenRespuestaIncorrecta1 = ordenrespuestaincorrecta1, ordenRespuestaIncorrecta2 = ordenrespuestaincorrecta2, Evaluacion = evaluacion)
        evaluacionItem.save()

        response_data['result'] = 'Pregunta Creada!'
        response_data['idPregunta'] = evaluacionItem.id
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def GuardarPregunta(request):
    if request.method == 'POST':
        
        response_data = {}
        preguntaId = request.POST['preguntaId']
        evaluacionItem = EvaluacionItem.objects.get(pk=preguntaId)
        
        pregunta = request.POST['pregunta']
        respuestacorrecta = request.POST['respuestacorrecta']
        respuestaincorrecta1 = request.POST['respuestaincorrecta1']
        respuestaincorrecta2 = request.POST['respuestaincorrecta2']
        ordenrespuestacorrecta = request.POST['ordenrespuestacorrecta']
        ordenrespuestaincorrecta1 = request.POST['ordenrespuestaincorrecta1']
        ordenrespuestaincorrecta2 = request.POST['ordenrespuestaincorrecta2']
        
        evaluacionItem.pregunta = pregunta
        evaluacionItem.respuestaCorrecta = respuestacorrecta
        evaluacionItem.respuestaIncorrecta1 = respuestaincorrecta1
        evaluacionItem.respuestaIncorrecta2 = respuestaincorrecta2
        evaluacionItem.ordenRespuestaCorrecta = ordenrespuestacorrecta
        evaluacionItem.ordenRespuestaIncorrecta1 = ordenrespuestaincorrecta1
        evaluacionItem.ordenRespuestaIncorrecta2 = ordenrespuestaincorrecta2
        evaluacionItem.save()

        response_data['result'] = 'Pregunta Editada!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def TraerPregunta(request):
    if request.method == 'POST':
        
        response_data = {}
        preguntaId = request.POST['preguntaId']
        evaluacionItem = EvaluacionItem.objects.get(pk=preguntaId)


        response_data['result'] = 'Pregunta Creada!'
        response_data['pregunta'] = evaluacionItem.pregunta
        response_data['respuestacorrecta'] = evaluacionItem.respuestaCorrecta
        response_data['respuestaincorrecta1'] = evaluacionItem.respuestaIncorrecta1
        response_data['respuestaincorrecta2'] = evaluacionItem.respuestaIncorrecta2
        response_data['ordenrespuestacorrecta'] = evaluacionItem.ordenRespuestaCorrecta
        response_data['ordenrespuestaincorrecta1'] = evaluacionItem.ordenRespuestaIncorrecta1
        response_data['ordenrespuestaincorrecta2'] = evaluacionItem.ordenRespuestaIncorrecta2
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return JsonResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def EliminarPregunta(request):
    if request.method == 'POST':
        
        response_data = {}
        
        preguntaId = request.POST['preguntaId']
        pregunta = EvaluacionItem.objects.get(pk=preguntaId)
        pregunta.delete()

        response_data['result'] = 'Pregunta Eliminada!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def TraerDatosObjeto(request):
    if request.method == 'POST':
        oaid = int(request.POST['oaid'])
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        objetoJson = serializers.serialize('json', [oa])
        patronJson = serializers.serialize('json', [oa.PatronPedagogico])
        
        
        if oa.Evaluacion != None:
            evaluacion = oa.Evaluacion
            evaluacionItems = oa.Evaluacion.evaluacionitem_set.all()
            evaluacionJson = serializers.serialize('json', [evaluacion])
            evaluacionItemsJson = serializers.serialize('json', evaluacionItems)
        else:
            evaluacion = []
            evaluacionItems = []
            evaluacionJson = serializers.serialize('json', evaluacion)
            evaluacionItemsJson = serializers.serialize('json', evaluacionItems)
            
        verdaderosFalsosJson = serializers.serialize('json', VerdaderoFalso.objects.filter(ObjetoAprendizaje=oa))
        identificacionesJson = serializers.serialize('json', Identificacion.objects.filter(ObjetoAprendizaje=oa))
        asociacionesJson = serializers.serialize('json', Asociacion.objects.filter(ObjetoAprendizaje=oa))
        videosJson = serializers.serialize('json', Video.objects.filter(ObjetoAprendizaje=oa))
        ordenamientosJson = serializers.serialize('json', Ordenamiento.objects.filter(ObjetoAprendizaje=oa))
        
        seccionesContenidoJson = serializers.serialize('json', oa.seccioncontenido_set.all())
        seccionesNombreJson = serializers.serialize('json', oa.PatronPedagogico.seccionnombre_set.all())

        return JsonResponse(
            {'objeto':objetoJson,
             'patron': patronJson,
             'evaluacion':evaluacionJson,
             'evaluacionItems':evaluacionItemsJson,
             'verdaderofalso': verdaderosFalsosJson,
             'identificacion': identificacionesJson,
             'asociacion': asociacionesJson,
             'video': videosJson,
             'ordenamiento': ordenamientosJson,
             'seccionesNombre':seccionesNombreJson,
             'seccionesContenido': seccionesContenidoJson},
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def TraerTerminosEvaluacion(request):
    if request.method == 'POST':
        
        
        evaluacionId = request.POST['evaluacionid']
        evaluacion = Evaluacion.objects.get(pk=evaluacionId)
        
        terminos = evaluacion.evaluacionitem_set.all()
        
        terminosJson = serializers.serialize('json', terminos)

        return JsonResponse(
            {'enunciado':evaluacion.enunciado,'terminos': terminosJson},
            content_type="application/json"
        )
    else:
        return JsonResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
    
        