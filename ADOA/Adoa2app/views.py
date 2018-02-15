# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from Adoa2app.models.ObjetoAprendizaje import ObjetoAprendizaje,\
    SeccionContenido
import json
from Adoa2app.models.PatronPedagogico import PatronPedagogico, SeccionNombre
from Adoa2app.models.Categoria import Categoria

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
from Adoa2app.models import Usuario
from operator import itemgetter, attrgetter, methodcaller
from Adoa2app.usuario.access import my_access_required

class Index(TemplateView):
    template_name = 'Index.html'
    
class LogOn(TemplateView):
    template_name = 'LogOn.html'

@my_access_required    
def CrearOA(request):
    model = ObjetoAprendizaje
    template_name = 'CrearOA.html'

    usuario = request.session['usuario']
    
    return render_to_response(template_name, locals(), context_instance = RequestContext(request))  

def BorrarOA(request, objId):
    response_data = {}
    try:
        oa = ObjetoAprendizaje.objects.get(id = objId)
        oa.delete()
        
        response_data['code'] = True
        response_data['result'] = 'Objeto de Aprendizaje borrado!'
    except:
        response_data['code'] = False
        response_data['result'] = 'Error al borrar el objeto!'
            
    return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

@my_access_required
def EditarOA(request, objId):
    try:
        objeto = ObjetoAprendizaje.objects.get(pk=objId)
    except ObjetoAprendizaje.DoesNotExist:
        raise Http404("Poll does not exist")
    id = request.session['usuario'].id
    return render(request, 'CrearOA.html', {'id': id, 'objeto': objeto})

def Objetos(request, operacion):
    id = request.session['usuario'].id
    return render(request, 'Objetos.html', {'id' : id, 'operacion': operacion})

def Objetos2(request, operacion):
    id = request.session['usuario'].id
    return render(request, 'ObjetosInicio.html', {'id' : id, 'operacion': operacion})

#Creamos secciones vacias para el OA
def crearSecciones(oa):
    seccionNombre = SeccionNombre.objects.filter(PatronPedagogico = oa.PatronPedagogico)
    for seccion in seccionNombre:
        seccionContenido = SeccionContenido()
        seccionContenido.ObjetoAprendizaje = oa
        seccionContenido.SeccionNombre = seccion
        seccionContenido.save()
    
def Paso1(request):
    if request.method == 'POST':
        response_data = {}
        oaid = int(request.POST['oaid'])
        if oaid==0:
            oatitulo = request.POST['titulo']
            oadescripcion = request.POST['descripcion']

            patron = request.POST['patron']
            oapatron = PatronPedagogico.objects.get(pk=patron)

            usuario = request.session['usuario']

            categoria = request.POST['categoria']
            oacategoria = Categoria.objects.get(pk=categoria)

            oa = ObjetoAprendizaje(titulo = oatitulo, descripcion = oadescripcion, PatronPedagogico = oapatron, Usuario = usuario, Categoria = oacategoria)
            oa.save()
            evaluacion = Evaluacion(ObjetoAprendizaje = oa)
            evaluacion.save()
            crearSecciones(oa)
            response_data['result'] = 'Objeto de Aprendizaje Creado!'
        else:
            oa = ObjetoAprendizaje.objects.get(pk=oaid)
            oa.titulo = request.POST['titulo']
            oa.descripcion = request.POST['descripcion']
            patron = request.POST['patron']
            categoria = request.POST['categoria']
            
            #Si cambia el patron, borramos las secciones guardadas y creamos nuevas vacias
            if oa.PatronPedagogico.id != patron:
                seccionContenido = SeccionContenido.objects.filter(ObjetoAprendizaje = oa)
                listaSecciones = list(seccionContenido)
                k = len(listaSecciones)
                for i in range(0, k):
                    listaSecciones[i].delete()
                    
                oa.PatronPedagogico = PatronPedagogico.objects.get(pk=patron)
                oa.Categoria = Categoria.objects.get(pk=categoria)
                crearSecciones(oa)
                
            oa.save()
            response_data['result'] = 'Objeto de Aprendizaje Editado!'
             
        response_data['evaluacionid'] = Evaluacion.objects.get(ObjetoAprendizaje = oa).id
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
        seccionesObjeto = SeccionContenido.objects.filter(ObjetoAprendizaje = oa)
        
        i = 0
        for seccion in seccionesObjeto:
            seccion.contenido = secciones[i]['contenido']
            seccion.ObjetoAprendizaje = oa
            seccion.save()
            i+=1
            
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

def TraerCategorias(request):
    if request.method == 'POST':
        
        categorias = Categoria.objects.all()
        categoriasJson = serializers.serialize('json', categorias)

        return HttpResponse(
            categoriasJson,
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
        nombreactividad = request.POST['nombreactividad']
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        
        verdaderoFalso = VerdaderoFalso(ObjetoAprendizaje = oa, nombre = nombreactividad)
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
        nombreactividad = request.POST['nombreactividad']
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        
        identificacion = Identificacion(ObjetoAprendizaje = oa, nombre = nombreactividad)
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
        nombreactividad = request.POST['nombreactividad']
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        
        ordenamiento = Ordenamiento(ObjetoAprendizaje = oa, nombre = nombreactividad)
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
        nombreactividad = request.POST['nombreactividad']
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        
        asociacion = Asociacion(ObjetoAprendizaje = oa, nombre = nombreactividad)
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
            asociacionItem = AsociacionItem(campo1 = termino['campo1'],campo2 = termino['campo2'],ordenCampo1 = termino['ordenCampo1'],ordenCampo2 = termino['ordenCampo2'])
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
        nombreactividad = request.POST['nombreactividad']
        oa = ObjetoAprendizaje.objects.get(pk=oaid)
        
        video = Video(ObjetoAprendizaje = oa, nombre = nombreactividad)
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
        
def TraerMisObjetos(request):
    if request.method == 'POST':
        
        response_data = {}
        #idUsuario = request.session['usuario']
        objetos = ObjetoAprendizaje.objects.filter(
        Usuario = request.session['usuario']
        )
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

def mostrarObjetosSinTerminar(request):

    if request.method == 'POST':
        
        response_data = {}
        
        #oa = ObjetoAprendizaje.objects.all()
        oa = ObjetoAprendizaje.objects.filter(
        Usuario = request.session['usuario']
        )
        objetos = []
        patrones = []
        categorias = []

        for registro in oa:
            oaCompleto = esExportable(registro)
            if not oaCompleto[0]:
                objetos.append(registro)
                patrones.append(registro.PatronPedagogico)
                categorias.append(registro.Categoria)
            
        objetosJson = serializers.serialize('json', objetos)
        patronesJson = serializers.serialize('json', patrones)
        categoriasJson = serializers.serialize('json', categorias)
        response_data['objetos'] = objetosJson

        response_data['patrones'] = patronesJson

        response_data['categorias'] = categoriasJson
        return JsonResponse(
            response_data,
          
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
        categoriaJson = serializers.serialize('json', [oa.Categoria])
        evaluacionOA = Evaluacion.objects.get(ObjetoAprendizaje = oa)
        
        if evaluacionOA is not None:
            evaluacionItems = evaluacionOA.evaluacionitem_set.all()
            evaluacionJson = serializers.serialize('json', [evaluacionOA])
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
        
        usuarioJson = serializers.serialize('json', [oa.Usuario])
        return JsonResponse(
            {'objeto':objetoJson,
             'patron': patronJson,
             'categoria': categoriaJson,
             'evaluacion':evaluacionJson,
             'evaluacionItems':evaluacionItemsJson,
             'verdaderofalso': verdaderosFalsosJson,
             'identificacion': identificacionesJson,
             'asociacion': asociacionesJson,
             'video': videosJson,
             'ordenamiento': ordenamientosJson,
             'seccionesNombre':seccionesNombreJson,
             'seccionesContenido': seccionesContenidoJson,
             'usuario': usuarioJson},
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


def ExportarOA(request, objId):
    try:
        import zipfile
        import StringIO
        from django.conf import settings
        import sys
        
        reload(sys)
        oa = ObjetoAprendizaje.objects.get(pk=objId)
        sys.setdefaultencoding("ISO-8859-1")
        filename = oa.titulo.replace(' ', '_') + '.zip'
        s = StringIO.StringIO()
        #z = zipfile.ZipFile(s, 'w')
        zf = zipfile.ZipFile(s, "w", zipfile.ZIP_DEFLATED,False)
        #zf = zipfile.ZipFile(filename,mode='w',compression=zipfile.ZIP_DEFLATED)

        zf.writestr("imsmanifest.xml" , manifestXml(oa) )
        zf.writestr("introduccion.html", crearIntroduccion(oa))
        zf.writestr("contenido.html", crearContenido(oa))
        zf.writestr("evaluacion.html", crearEvalucion(oa))
        
        
        verdaderosFalsos = VerdaderoFalso.objects.filter(ObjetoAprendizaje=oa)
        identificaciones = Identificacion.objects.filter(ObjetoAprendizaje=oa)
        asociaciones = Asociacion.objects.filter(ObjetoAprendizaje=oa)
        videos = Video.objects.filter(ObjetoAprendizaje=oa)
        ordenamientos = Ordenamiento.objects.filter(ObjetoAprendizaje=oa)
        for actividad in verdaderosFalsos:
            zf.writestr("actividad"+str(actividad.id)+".html", crearVerdaderoFalsoScorm(actividad))
        for actividad in identificaciones:
            zf.writestr("actividad"+str(actividad.id)+".html", crearIdentificacionScorm(actividad))
        for actividad in asociaciones:
            zf.writestr("actividad"+str(actividad.id)+".html", crearAsociacionScorm(actividad))
        for actividad in videos:
            zf.writestr("actividad"+str(actividad.id)+".html", crearVideoScorm(actividad))
        for actividad in ordenamientos:
            zf.writestr("actividad"+str(actividad.id)+".html", crearOrdenamientoScorm(actividad))
            

        #----------------------ARCHIVOS ESTATICOS------------------------------
        staticDir = settings.STATICFILES_DIRS[0];
        
        pathfile = staticDir + "/stylesheets/materialize/css"
        abrirAch=open(pathfile+"/EstiloScorm.css","r" )
        zf.writestr("css/EstiloScorm.css",abrirAch.read())
        
        pathfile = staticDir + "/stylesheets/materialize/js/Objeto"
        abrirAch=open(pathfile+"/VisualizacionActividades.js","r" )
        zf.writestr("Actividades.js",abrirAch.read())

        pathfile = staticDir + "/stylesheets/materialize/js/Objeto"
        abrirAch=open(pathfile+"/VisualizacionEvaluacion.js","r" )
        zf.writestr("Evaluacion.js",abrirAch.read())
        
        pathfile = staticDir + "/stylesheets/materialize/js"
        abrirAch=open(pathfile+"/jquery-2.1.1.min.js","r" )
        zf.writestr("jquery-2.1.1.min.js",abrirAch.read())
        
        pathfile = staticDir + "/stylesheets/materialize/css"
        abrirAch=open(pathfile+"/materialize.min.css","r" )
        zf.writestr("css/materialize.min.css",abrirAch.read())
        
        pathfile = staticDir + "/stylesheets/materialize/js"
        abrirAch=open(pathfile+"/materialize.min.js","r" )
        zf.writestr("materialize.min.js",abrirAch.read())

        pathfile = staticDir + "/stylesheets/materialize/js/scorm"
        abrirAch=open(pathfile+"/SCOFunctions.js","r" )
        zf.writestr("SCOFunctions.js",abrirAch.read())

        pathfile = staticDir + "/stylesheets/materialize/js/scorm"
        abrirAch=open(pathfile+"/SCORM_API_wrapper.js","r" )
        zf.writestr("SCORM_API_wrapper.js",abrirAch.read())
        
        
#===============================================================================
#         
#         pathfile = "/home/adoa2016/Documents/LiClipse Workspace/Adoa2/ADOA/ADOA/Adoa2app/static/stylesheets/materialize/js/Objeto"
#         abrirAch=open(pathfile+"/VisualizacionActividades.js","r" )
#         zf.writestr("Actividades.js",abrirAch.read())
# 
#         pathfile = "/home/adoa2016/Documents/LiClipse Workspace/Adoa2/ADOA/ADOA/Adoa2app/static/stylesheets/materialize/js/Objeto"
#         abrirAch=open(pathfile+"/VisualizacionEvaluacion.js","r" )
#         zf.writestr("Evaluacion.js",abrirAch.read())
#         
#         pathfile = "/home/adoa2016/Documents/LiClipse Workspace/Adoa2/ADOA/ADOA/Adoa2app/static/stylesheets/materialize/js"
#         abrirAch=open(pathfile+"/jquery-2.1.1.min.js","r" )
#         zf.writestr("jquery-2.1.1.min.js",abrirAch.read())
#         
#         pathfile = "/home/adoa2016/Documents/LiClipse Workspace/Adoa2/ADOA/ADOA/Adoa2app/static/stylesheets/materialize/css"
#         abrirAch=open(pathfile+"/materialize.min.css","r" )
#         zf.writestr("css/materialize.min.css",abrirAch.read())
#         
#         pathfile = "/home/adoa2016/Documents/LiClipse Workspace/Adoa2/ADOA/ADOA/Adoa2app/static/stylesheets/materialize/js"
#         abrirAch=open(pathfile+"/materialize.min.js","r" )
#         zf.writestr("materialize.min.js",abrirAch.read())
# 
#         pathfile = "/home/adoa2016/Documents/LiClipse Workspace/Adoa2/ADOA/ADOA/Adoa2app/static/stylesheets/materialize/js/scorm"
#         abrirAch=open(pathfile+"/SCOFunctions.js","r" )
#         zf.writestr("SCOFunctions.js",abrirAch.read())
# 
#         pathfile = "/home/adoa2016/Documents/LiClipse Workspace/Adoa2/ADOA/ADOA/Adoa2app/static/stylesheets/materialize/js/scorm"
#         abrirAch=open(pathfile+"/SCORM_API_wrapper.js","r" )
#         zf.writestr("SCORM_API_wrapper.js",abrirAch.read())
#===============================================================================

        #----------------------/ARCHIVOS ESTATICOS------------------------------

        #zf.writestr('prueba.txt', 'Hello, world')
        zf.close()
        
        resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
        
        resp['Content-Disposition'] = 'attachment; filename=%s' % filename
        return resp

    except ObjetoAprendizaje.DoesNotExist:
        raise Http404("Poll does not exist")
    return ""

def ComprobarOA(request, id):
    try:
        oa = ObjetoAprendizaje.objects.get(pk=id)
        sePuedeExportar = esExportable(oa)
        return JsonResponse(
                            json.dumps(sePuedeExportar[1]),
                            content_type="application/json",
                            safe = False
                            )
    except ObjetoAprendizaje.DoesNotExist:
        raise Http404("Poll does not exist")    
    
def inicioOA(request):
    '''
    oa = ObjetoAprendizaje.objects.all()
    model = ObjetoAprendizaje
    template_name = 'ObjetosInicio.html'
    lista = []

    for registro in oa:
        oaCompleto = esExportable(registro)
        if oaCompleto[0]:
            lista.append(registro)
        
    usuario = request.session['usuario']
    #lista = Usuario.objects.all()
    return render_to_response(template_name, locals(), context_instance = RequestContext(request))
    '''
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

    
def esExportable (oa):
    import collections
    attrOA = collections.OrderedDict([('Información', True), ('Introducción',True), ('Contenido',True), ('Actividad', True), ('Evaluación', True)])
    #attrOA = {'Informacion': True, 'Introduccion' : True, 'Contenido' : True, 'Actividad' : True, 'Evaluacion' : True}
    secciones = {'Exportable': True, 'attrOA':attrOA}
    oaCompleto = oa.estaCompleto()
    exportable = True
    if oaCompleto[0] is False:
        exportable = False
        for seccion in oaCompleto[1]:
            secciones['attrOA'][seccion] = False

    actividad = Actividad()
    actividad.ObjetoAprendizaje = oa
    actividades = actividad.getAll();
    listado = list(actividades)
    actividadCompleta = True
    kActiv = 0 #Cuento la cantidad de actividades
    i = 0    
    
    while actividadCompleta and len(listado) > i:
        lista = listado[i]
        j = 0
        while actividadCompleta and len(lista) > j:
            item = lista[j]
            kActiv+=1
            if item.estaCompleto() is False:
                actividadCompleta = False
                secciones['attrOA']['Actividad'] = False
                exportable = False
            j+=1
        i+=1   
    
    #Si no tiene actividades, se pone como incompleta
    if secciones['attrOA']['Actividad'] and kActiv < 1:
        secciones['attrOA']['Actividad'] = False
    
    secciones['Exportable'] = exportable
        
    return (exportable, secciones)

def paginaMaestra(seccion,contenido,scriptExtra):
    cadena = '<html>\n\
    <head>\n\
        <meta charset="utf-8"> \
        <link rel="stylesheet" type="text/css" href="css/materialize.min.css" media="screen" />\n\
        <link rel="stylesheet" type="text/css" href="css/EstiloScorm.css" media="screen" />\n\
        <script type="text/javascript" src="SCORM_API_wrapper.js"></script>\n\
        <script type="text/javascript" src="SCOFunctions.js"></script>\n\
        <script type="text/javascript" src="jquery-2.1.1.min.js"></script>\n\
        <script type="text/javascript" src="materialize.min.js"></script>\n\
        <script type="text/javascript" src="Actividades.js"></script>\n\
        <script type="text/javascript" src="Evaluacion.js"></script>\n\
        '+scriptExtra+'\
    </head>\n\
    <body onload="loadPage()" onunload="unloadPage()">\n\
        <script type="text/javascript">pipwerks.SCORM.data.set("cmi.completion_status","completed")</script>\n\
            <div id="pagina">\n\
                <blockquote><h4 class="titulo">'+seccion+'</h4></blockquote>\n\
                <div class="divider"></div>\n\
                <div class="cont">'+contenido+'\n\
                </div>\n\
            </div>\n\
    </body>\n\
</html>'
    return cadena

def manifestXml(oa):
    actividades = oa.actividad_set.all()
    verdaderosFalsos = VerdaderoFalso.objects.filter(ObjetoAprendizaje=oa)
    identificaciones = Identificacion.objects.filter(ObjetoAprendizaje=oa)
    asociaciones = Asociacion.objects.filter(ObjetoAprendizaje=oa)
    videos = Video.objects.filter(ObjetoAprendizaje=oa)
    ordenamientos = Ordenamiento.objects.filter(ObjetoAprendizaje=oa)
    
    cadena ='<manifest xmlns="http://www.imsglobal.org/xsd/imscp_v1p1" \
            xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_v1p3" \
            xmlns:adlseq="http://www.adlnet.org/xsd/adlseq_v1p3" \
            xmlns:adlnav="http://www.adlnet.org/xsd/adlnav_v1p3" \
            xmlns:imsss="http://www.imsglobal.org/xsd/imsss" \
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \
            identifier="com.scorm.manifesttemplates.scorm2004.4thEd.nometadata" version="1" \
            xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 imscp_v1p1.xsd\ http://www.adlnet.org/xsd/adlcp_v1p3 adlcp_v1p3.xsd http://www.adlnet.org/xsd/adlseq_v1p3 adlseq_v1p3.xsd http://www.adlnet.org/xsd/adlnav_v1p3 adlnav_v1p3.xsd http://www.imsglobal.org/xsd/imsss imsss_v1p0.xsd">\
    <metadata>\
            <schema>ADL SCORM</schema>\
        <schemaversion>2004 4th Edition</schemaversion>\
    </metadata>\
    <organizations default="B0">\
        <organization identifier="B0" adlseq:objectivesGlobalToSystem="false">\
            <!-- Titulo que se visuliza arriba de todo en el moodle-->\
            <title>'+oa.titulo+'</title>\
                <!--<item identifier="'+oa.titulo+'">-->\
                    <!--seccion de introduccion que se ve en moodle-->\
                    <item identifier="introduccion" identifierref="introduccion_resource">\
                        <title>Introduccion</title>\
                    </item>\
                    <!--seccion de contenido que se ve en moodle-->\
                    <item identifier="contenido" identifierref="contenido_resource">\
                        <title>Contenido</title>\
                    </item>'
    
    for actividad in verdaderosFalsos:
        cadena+='<!--seccion de actividades que se ve en moodle-->\
            <item identifier="actividad'+str(actividad.id)+'" identifierref="actividad'+str(actividad.id)+'_resource">\
                <title>'+actividad.nombre+'</title>\
            </item>'
    for actividad in identificaciones:
        cadena+='<!--seccion de actividades que se ve en moodle-->\
            <item identifier="actividad'+str(actividad.id)+'" identifierref="actividad'+str(actividad.id)+'_resource">\
                <title>'+actividad.nombre+'</title>\
            </item>'
    for actividad in asociaciones:
        cadena+='<!--seccion de actividades que se ve en moodle-->\
            <item identifier="actividad'+str(actividad.id)+'" identifierref="actividad'+str(actividad.id)+'_resource">\
                <title>'+actividad.nombre+'</title>\
            </item>'
    for actividad in videos:
        cadena+='<!--seccion de actividades que se ve en moodle-->\
            <item identifier="actividad'+str(actividad.id)+'" identifierref="actividad'+str(actividad.id)+'_resource">\
                <title>'+actividad.nombre+'</title>\
            </item>'
    for actividad in ordenamientos:
        cadena+='<!--seccion de actividades que se ve en moodle-->\
            <item identifier="actividad'+str(actividad.id)+'" identifierref="actividad'+str(actividad.id)+'_resource">\
                <title>'+actividad.nombre+'</title>\
            </item>'
                
    cadena +='<!--seccion de evalucion que se ve en moodle-->\
                    <item identifier="evaluacion" identifierref="evalucion_resource">\
                        <title>Evaluacion</title>\
                    </item>\
            <!--</item>-->\
        </organization>\
    </organizations>\
    <resources>\
        <!-- contenido de la seccion introduccion -->\
        <resource identifier="introduccion_resource" type="webcontent" adlcp:scormType="sco" href="introduccion.html">\
            <file href="introduccion.html"/>\
        </resource>\
        <!-- contenido de la seccion contenido -->\
        <resource identifier="contenido_resource" type="webcontent" adlcp:scormType="sco" href="contenido.html">\
            <file href="contenido.html"/>\
        </resource>'
    for actividad in actividades:
        cadena+='<!-- contenido de la seccion actividades -->\
        <resource identifier="actividad'+str(actividad.id)+'_resource" type="webcontent" adlcp:scormType="sco" href="actividad'+str(actividad.id)+'.html">\
            <file href="actividad'+str(actividad.id)+'.html"/>\
        </resource>'
        
    cadena+='<!-- contenido de la seccion evaluacion -->\
        <resource identifier="evalucion_resource" type="webcontent" adlcp:scormType="sco" href="evaluacion.html">\
            <file href="evaluacion.html"/>\
        </resource>\
        <!--Archivos comunes para todos los contenidos -->\
        <resource identifier="common_files" type="webcontent" adlcp:scormType="asset">\
            <file href="css/materialize.min.css"/>\
            <file href="css/EstiloScorm.css"/>\
            <file href="jquery-2.1.1.min.js"/>\
            <file href="SCOFunctions.js"/>\
            <file href="Evaluacion.js"/>\
            <file href="Actividades.js"/>\
            <file href="SCORM_API_wrapper.js"/>\
            <file href="materialize.min.js"/>\
        </resource>\
    </resources>\
</manifest>'
    return cadena

def crearIntroduccion(objeto):
    contenido="<div>"+objeto.descripcion+"</div>"
    contenido += "<div>" + objeto.introduccion + "</div>"
    return paginaMaestra("Introduccion",contenido.encode('utf-8'),"")

def crearContenido(objeto):
    contenido = ""
    
    patron = PatronPedagogico.objects.get(id = objeto.PatronPedagogico_id)

    seccionNom = SeccionNombre.objects.filter(PatronPedagogico= patron)

    ####Aca tengo todo
    seccionCon = SeccionContenido.objects.filter(SeccionNombre= seccionNom,ObjetoAprendizaje=objeto)

    ####Aca tengo todo
    for seccion in seccionCon:
        contenido+= "<h5>" + seccion.SeccionNombre.nombre + "</h5>"
        contenido+= "<div>" + seccion.contenido + "</div>"
        
    return paginaMaestra("Contenido",contenido.encode('utf-8'),"")

def crearVerdaderoFalsoScorm(actividad):

    script = ''
    
    actividadItems = actividad.verdaderofalsoitem_set.all()
    contenido= ""
    contenido+="<div class='col s12'>"\
        "<p><b>"+actividad.enunciado+"</b></p>"\
    "</div>"
    
    for item in actividadItems:
        contenido+="<div class='row'>"\
                        "<div class='col s6'>"\
                            "<p>"+item.afirmacion+"</p>"\
                        "</div>"\
                        "<div class='input-field col s3'>"\
                            "<select id='selectVerdaderoFalso"+str(item.id)+"' class='selectVerdaderoFalso' name='selectVerdaderoFalso'>"\
                                "<option value='' disabled='' selected=''>Seleccione la respuesta</option>"\
                                "<option value='0' >Falso</option>"\
                                "<option value='1' >Verdadero</option>"\
                            "</select>"\
                            "<label>Respuesta</label>"\
                        "</div>"\
                        "<div class='col s3' id='resultado"+str(item.id)+"'>"\
                        "</div>"\
                    "</div>"
        if item.respuesta == True:
            contenido+="<input type='hidden' class='respuestaVerdaderoFalso' name='respuesta"+str(item.id)+"' data-id='"+str(item.id)+"' id='respuesta"+str(item.id)+"' value='1'>"
        else:
            contenido+="<input type='hidden' class='respuestaVerdaderoFalso' name='respuesta"+str(item.id)+"' data-id='"+str(item.id)+"' id='respuesta"+str(item.id)+"' value='0'>"
        
    contenido+="<div class='row col s12'>"\
                    "<a class='btn waves-effect waves-light left red' onclick='validarRespuestasVerdaderoFalso()'>Correccion</a>"\
                "</div>"
    contenido+="<script>$('select').material_select();</script>"

    return paginaMaestra(actividad.nombre, contenido.encode('utf-8'),script)

def crearIdentificacionScorm(actividad):
    script = ''
    
    actividadItems = actividad.identificacionitem_set.all()
    contenido= ""

    contenido+="<div class='col s12'>"\
        "<p><b>"+actividad.enunciado+"</b></p>"\
    "</div>"

    script = ''
    for item in actividadItems:
        contenido+="<div class='row'>"\
                        "<div class='col s6'>"\
                            "<p>"+item.concepto+"</p>"\
                        "</div>"\
                        "<div class='input-field col s3'>"\
                            "<select id='selectIdentificacion"+str(item.id)+"' class='selectIdentificacion' name='selectIdentificacion'>"\
                                "<option value='' disabled='' selected=''>Seleccione si corresponde</option>"\
                                "<option value='0' >No</option>"\
                                "<option value='1' >Si</option>"\
                            "</select>"\
                            "<label>Corresponde</label>"\
                        "</div>"\
                        "<div class='col s3' id='resultado"+str(item.id)+"'>"\
                        "</div>"\
                    "</div>"
        if item.respuesta == True:
            contenido+="<input type='hidden' class='respuestaIdentificacion' name='respuesta"+str(item.id)+"' data-id='"+str(item.id)+"' id='respuesta"+str(item.id)+"' value='1'>"
        else:
            contenido+="<input type='hidden' class='respuestaIdentificacion' name='respuesta"+str(item.id)+"' data-id='"+str(item.id)+"' id='respuesta"+str(item.id)+"' value='0'>"
        
    contenido+="<div class='row col s12'>"\
                    "<a class='btn waves-effect waves-light left red' onclick='validarRespuestasIdentificacion()'>Correccion</a>"\
                "</div>"
    contenido+="<script>$('select').material_select();</script>"

    return paginaMaestra(actividad.nombre, contenido.encode('utf-8'),script)

def crearOrdenamientoScorm(actividad):

    script = ''
    
    actividadItems = actividad.ordenamientoitem_set.all()
    contenido= ""

    contenido+="<div class='col s12'>"\
        "<p><b>"+actividad.enunciado+"</b></p>"\
    "</div>"

    script = ''

    for item in actividadItems:
        contenido+="<div class='row'>"\
                        "<div class='col s6'>"\
                            "<p>"+item.texto+"</p>"\
                        "</div>"\
                        "<div class='input-field col s3'>"\
                            "<select id='selectOrdenamiento"+str(item.id)+"' class='selectOrdenamiento' name='selectOrdenamiento'>"\
                                "<option value='' disabled='' selected=''>Seleccione el orden</option>"\
                                "<option value='1'>1</option>"\
                                "<option value='2'>2</option>"\
                                "<option value='3'>3</option>"\
                                "<option value='4'>4</option>"\
                                "<option value='5'>5</option>"\
                                "<option value='6'>6</option>"\
                                "<option value='7'>7</option>"\
                                "<option value='8'>8</option>"\
                                "<option value='9'>9</option>"\
                                "<option value='10'>10</option>"\
                            "</select>"\
                            "<label>Orden</label>"\
                        "</div>"\
                        "<input type='hidden' class='respuestaOrdenamiento' name='respuesta"+str(item.id)+"' data-id='"+str(item.id)+"' id='respuesta"+str(item.id)+"' value='"+str(item.orden)+"'>"\
                        "<div class='col s3' id='resultado"+str(item.id)+"'>"\
                        "</div>"\
                    "</div>"
                    
        
        
    contenido+="<div class='row col s12'>"\
                    "<a class='btn waves-effect waves-light left red' onclick='validarRespuestasOrdenamiento()'>Correccion</a>"\
                "</div>"
    contenido+="<script>$('select').material_select();</script>"

    return paginaMaestra(actividad.nombre, contenido.encode('utf-8'),script)

def crearVideoScorm(actividad):

    contenido = ""
    script = ''
    
    contenido += "<div class='row'>"\
            "<div class='offset-s2 col s8'>"\
                "<div class='video-container'>"\
                    + embeberVideo(actividad.link) +\
                "</div>"\
            "</div>"\
            "<div class='col s12'>"\
                "<p><b>"+actividad.descripcion+"</b></p>"\
            "</div>"\
            "</div>"

    return paginaMaestra(actividad.nombre, contenido.encode('utf-8'),script)

def crearAsociacionScorm(actividad):

    script = ''
    
    actividadItems = actividad.asociacionitem_set.all()
    contenido= ""

    contenido+="<div class='col s12'>"\
        "<p><b>"+actividad.enunciado+"</b></p>"\
    "</div>"

    script = ''
    contador = 0
    listaCampoOrden1 = []
    listaCampoOrden2 = []
    ordenada = []
    ordenada2 = []

    for item in actividadItems:
        listaCampoOrden1.append(AsociacionItem(campo1 = item.campo1,campo2 = "",ordenCampo1 = item.ordenCampo1,ordenCampo2 = ""));
        listaCampoOrden2.append(AsociacionItem(campo1 = "",campo2 = item.campo2,ordenCampo1 = "",ordenCampo2 = item.ordenCampo2));

    ordenada = sorted(listaCampoOrden1, key=attrgetter('ordenCampo1'))
    ordenada2 = sorted(listaCampoOrden2, key=attrgetter('ordenCampo2'))  
        
    
    for item in actividadItems:
        contador = contador + 1
        contenido+="<div class='row'>"\
                    "<div class='col s12'>"\
                        "<div id='campo1-"+str(contador)+"' class='col s4'>"\
                            "<h3>Item "+str(ordenada[contador-1].ordenCampo1)+"</h3>"\
                            +ordenada[contador-1].campo1+\
                        "</div>"\
                        "<div id='contenedor-"+str(contador)+"' class='col s3'>"\
                            "<div class='input-field col s10'>"\
                                "<select id='selectAsociacion"+str(contador)+"' class='selectAsociacion' name='selectAsociacion'>"\
                                    "<option value='' disabled='' selected=''>Opciones</option>"\
                                    "<option value='1'>Item 1</option>"\
                                    "<option value='2'>Item 2</option>"\
                                    "<option value='3'>Item 3</option>"\
                                    "<option value='4'>Item 4</option>"\
                                    "<option value='5'>Item 5</option>"\
                                    "<option value='6'>Item 6</option>"\
                                    "<option value='7'>Item 7</option>"\
                                    "<option value='8'>Item 8</option>"\
                                    "<option value='9'>Item 9</option>"\
                                    "<option value='10'>Item 10</option>"\
                                "</select>"\
                                "<label>Asociar a</label>"\
                            "</div>"\
                            "<div id='resultado"+str(contador)+"' col s10'>"\
                            "</div>"\
                            "<input type='hidden' class='respuestaAsociacion' name='respuesta"+str(ordenada[contador-1].ordenCampo1)+"' data-id='"+str(ordenada[contador-1].ordenCampo1)+"' id='respuesta"+str(ordenada[contador-1].ordenCampo1)+"' value='"+str(ordenada2[contador-1].ordenCampo2)+"'>"\
                        "</div>"\
                        "<div id='campo2-"+str(contador)+"' class='col s4'>"\
                            "<h3>Item "+str(ordenada2[contador-1].ordenCampo2)+"</h3>"\
                            +ordenada2[contador-1].campo2+\
                        "</div>"\
                        "</div>"\
                    "</div>"
        
        
    contenido+="<div class='row col s12'>"\
                    "<a class='btn waves-effect waves-light left red' onclick='validarRespuestasAsociacion()'>Correccion</a>"\
                "</div>"
    contenido+="<script>$('select').material_select();</script>"

    return paginaMaestra(actividad.nombre, contenido.encode('utf-8'),script)

def crearEvalucion(oa):
    script=''
    
    evaluacionOA = Evaluacion.objects.get(ObjetoAprendizaje = oa)            
    evaluacionItems = evaluacionOA.evaluacionitem_set.all()
    contenido= ""
    for pregunta in evaluacionItems:
        contenido+="<div class='row col s10'>"\
                "<div class='col s9'>"\
                    "<b>"+pregunta.pregunta+"</b>"\
                "</div>"\
                "<div class='col s3' id='resultado"+str(pregunta.id)+"'>"\
                "</div>"
        if pregunta.ordenRespuestaCorrecta == 1:
            contenido+="<div class='col s12'>"\
                            "<div class='col s9'>"\
                                "<p id='respuesta1-"+str(pregunta.id)+"'>"+pregunta.respuestaCorrecta+"</p>"\
                            "</div>"\
                            "<div class='col s3'>"\
                                "<p>"\
                                    "<input name='group1"+str(pregunta.id)+"' type='radio' data-id='"+str(pregunta.id)+"' class='correcta' id='radiorespuesta1-"+str(pregunta.id)+"' />"\
                                    "<label for='radiorespuesta1-"+str(pregunta.id)+"'></label>"\
                                "</p>"\
                            "</div>"\
                        "</div>"
        elif pregunta.ordenRespuestaIncorrecta1 == 1:
            contenido+="<div class='col s12'>"\
                            "<div class='col s9'>"\
                                "<p id='respuesta2-"+str(pregunta.id)+"'>"+pregunta.respuestaIncorrecta1+"</p>"\
                            "</div>"\
                            "<div class='col s3'>"\
                                "<p>"\
                                    "<input name='group1"+str(pregunta.id)+"' type='radio' data-id='"+str(pregunta.id)+"' id='radiorespuesta2-"+str(pregunta.id)+"' />"\
                                    "<label for='radiorespuesta2-"+str(pregunta.id)+"'></label>"\
                                "</p>"\
                            "</div>"\
                        "</div>"
        elif pregunta.ordenRespuestaIncorrecta2 == 1:
            contenido+="<div class='col s12'>"\
                            "<div class='col s9'>"\
                                "<p id='respuesta3-"+str(pregunta.id)+"'>"+pregunta.respuestaIncorrecta2+"</p>"\
                            "</div>"\
                            "<div class='col s3'>"\
                                "<p >"\
                                    "<input name='group1"+str(pregunta.id)+"' type='radio' data-id='"+str(pregunta.id)+"' id='radiorespuesta3-"+str(pregunta.id)+"' />"\
                                    "<label for='radiorespuesta3-"+str(pregunta.id)+"'></label>"\
                                "</p>"\
                            "</div>"\
                        "</div>"
        if pregunta.ordenRespuestaCorrecta == 2:
            contenido+="<div class='col s12'>"\
                            "<div class='col s9'>"\
                                "<p id='respuesta1-"+str(pregunta.id)+"'>"+pregunta.respuestaCorrecta+"</p>"\
                            "</div>"\
                            "<div class='col s3'>"\
                                "<p>"\
                                    "<input name='group1"+str(pregunta.id)+"' type='radio' data-id='"+str(pregunta.id)+"' class='correcta' id='radiorespuesta1-"+str(pregunta.id)+"' />"\
                                    "<label for='radiorespuesta1-"+str(pregunta.id)+"'></label>"\
                                "</p>"\
                            "</div>"\
                        "</div>"
        elif pregunta.ordenRespuestaIncorrecta1 == 2:
            contenido+="<div class='col s12'>"\
                            "<div class='col s9'>"\
                                "<p id='respuesta2-"+str(pregunta.id)+"'>"+pregunta.respuestaIncorrecta1+"</p>"\
                            "</div>"\
                            "<div class='col s3'>"\
                                "<p>"\
                                    "<input name='group1"+str(pregunta.id)+"' type='radio' data-id='"+str(pregunta.id)+"' id='radiorespuesta2-"+str(pregunta.id)+"' />"\
                                    "<label for='radiorespuesta2-"+str(pregunta.id)+"'></label>"\
                                "</p>"\
                            "</div>"\
                        "</div>"
        elif pregunta.ordenRespuestaIncorrecta2 == 2:
            contenido+="<div class='col s12'>"\
                            "<div class='col s9'>"\
                                "<p id='respuesta3-"+str(pregunta.id)+"'>"+pregunta.respuestaIncorrecta2+"</p>"\
                            "</div>"\
                            "<div class='col s3'>"\
                                "<p >"\
                                    "<input name='group1"+str(pregunta.id)+"' type='radio' data-id='"+str(pregunta.id)+"' id='radiorespuesta3-"+str(pregunta.id)+"' />"\
                                    "<label for='radiorespuesta3-"+str(pregunta.id)+"'></label>"\
                                "</p>"\
                            "</div>"\
                        "</div>"
        if pregunta.ordenRespuestaCorrecta == 3:
            contenido+="<div class='col s12'>"\
                            "<div class='col s9'>"\
                                "<p id='respuesta1-"+str(pregunta.id)+"'>"+pregunta.respuestaCorrecta+"</p>"\
                            "</div>"\
                            "<div class='col s3'>"\
                                "<p>"\
                                    "<input name='group1"+str(pregunta.id)+"' type='radio' data-id='"+str(pregunta.id)+"' class='correcta' id='radiorespuesta1-"+str(pregunta.id)+"' />"\
                                    "<label for='radiorespuesta1-"+str(pregunta.id)+"'></label>"\
                                "</p>"\
                            "</div>"\
                        "</div>"
        elif pregunta.ordenRespuestaIncorrecta1 == 3:
            contenido+="<div class='col s12'>"\
                            "<div class='col s9'>"\
                                "<p id='respuesta2-"+str(pregunta.id)+"'>"+pregunta.respuestaIncorrecta1+"</p>"\
                            "</div>"\
                            "<div class='col s3'>"\
                                "<p>"\
                                    "<input name='group1"+str(pregunta.id)+"' type='radio' data-id='"+str(pregunta.id)+"' id='radiorespuesta2-"+str(pregunta.id)+"' />"\
                                    "<label for='radiorespuesta2-"+str(pregunta.id)+"'></label>"\
                                "</p>"\
                            "</div>"\
                        "</div>"
        elif pregunta.ordenRespuestaIncorrecta2 == 3:
            contenido+="<div class='col s12'>"\
                            "<div class='col s9'>"\
                                "<p id='respuesta3-"+str(pregunta.id)+"'>"+pregunta.respuestaIncorrecta2+"</p>"\
                            "</div>"\
                            "<div class='col s3'>"\
                                "<p >"\
                                    "<input name='group1"+str(pregunta.id)+"' type='radio' data-id='"+str(pregunta.id)+"' id='radiorespuesta3-"+str(pregunta.id)+"' />"\
                                    "<label for='radiorespuesta3-"+str(pregunta.id)+"'></label>"\
                                "</p>"\
                            "</div>"\
                        "</div>"
        
        contenido+="</div>"
        
    contenido+="<div class='row col s12'>"\
        "<a class='btn waves-effect waves-light left red' onclick='validarRespuestasEvaluacion()'>Correccion</a>"\
    "</div>"
    
    return paginaMaestra("Evaluacion",contenido.encode('utf-8'),script)


def importarOA(request, objId):
    response_data = {}
    try:
        usuario = request.session['usuario']
        oaOriginal = ObjetoAprendizaje.objects.get(id = objId)
        
        #Clona objeto de aprendizaje
        oaImportado = ObjetoAprendizaje()
        oaImportado.titulo = oaOriginal.titulo
        oaImportado.descripcion = oaOriginal.descripcion
        oaImportado.introduccion = oaOriginal.introduccion
        oaImportado.PatronPedagogico = oaOriginal.PatronPedagogico
        oaImportado.Usuario = usuario
        oaImportado.save()
        evaluacion = Evaluacion(ObjetoAprendizaje = oaImportado)
        evaluacion.save()
        
        #Clona la evaluacion
        evaluacionOriginal = Evaluacion.objects.get(ObjetoAprendizaje = oaOriginal)
        evaluacionItems = EvaluacionItem.objects.filter(Evaluacion = evaluacionOriginal)
        for evItem in evaluacionItems:
            evaluacionItem = EvaluacionItem()
            evaluacionItem.Evaluacion = evaluacion
            evaluacionItem.pregunta  = evItem.pregunta
            evaluacionItem.respuestaCorrecta = evItem.respuestaCorrecta
            evaluacionItem.respuestaIncorrecta1 = evItem.respuestaIncorrecta1
            evaluacionItem.respuestaIncorrecta2 = evItem.respuestaIncorrecta2
            evaluacionItem.ordenRespuestaCorrecta = evItem.ordenRespuestaCorrecta
            evaluacionItem.ordenRespuestaIncorrecta1 = evItem.ordenRespuestaIncorrecta1
            evaluacionItem.ordenRespuestaIncorrecta2 = evItem.ordenRespuestaIncorrecta2
            evaluacionItem.save()
        
        #Clona las actividades    
        actividad = Actividad()
        actividad.ObjetoAprendizaje = oaOriginal
        actividades = actividad.getAll()
        for lista in actividades:
            for actividad in lista:    
                actividad.clonar(oaImportado)
        
        
        #Clona las secciones
        seccionesOrigen = SeccionContenido.objects.filter(ObjetoAprendizaje = oaOriginal)
        for seccion in seccionesOrigen:
            seccionContenido = SeccionContenido(ObjetoAprendizaje = oaImportado)
            seccionContenido.contenido = seccion.contenido
            seccionContenido.SeccionNombre = seccion.SeccionNombre
            seccionContenido.save() 
                
        response_data['result'] = 'Objeto de aprendizaje importado correctamente!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
        
    except:
        response_data['result'] = 'Error al importar el objeto de aprendizaje!'
        
    return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )    
    
def embeberVideo(link):
    htmlGenerado = ""
    parametrosVideo = []
    url = 'url'
    indice = 'indice'
    regExp = 'regExp'
    frame = 'frame'
    match = '{match}'
    #youtube
    parametrosVideo.append({url: link, indice:1, regExp:r"^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$", frame:"<iframe allowfullscreen frameborder='0' src='//www.youtube.com/embed/" + match + "' width='640' height='360'></iframe>"})
    #instagram
    parametrosVideo.append({url: link, indice:0, regExp:r"(?:www\.|\/\/)instagram\.com\/p\/(.[a-zA-Z0-9_-]*)", frame:"<iframe allowfullscreen src = 'https://instagram.com/p/" + match + "/embed/' width='612' height='710' scrolling='true' allowtransparency='true'></iframe>"})
    #vine
    parametrosVideo.append({url: link, indice:0, regExp:r"\/\/vine\.co\/v\/([a-zA-Z0-9]+)", frame:"<iframe allowfullscreen frameborder='0' src = '" + match + "/embed/simple' width='600' height='600' class='vine-embed'></iframe>"})
    #vimeo
    parametrosVideo.append({url: link, indice:3, regExp:r"\/\/(player\.)?vimeo\.com\/([a-z]*\/)*([0-9]{6,11})[?]?.*", frame:"<iframe webkitallowfullscreen mozallowfullscreen allowfullscreen frameborder='0' src = '//player.vimeo.com/video/" + match + "' width='640' height='360'></iframe>"})
    #dailymotion
    parametrosVideo.append({url: link, indice:2, regExp:r".+dailymotion.com\/(video|hub)\/([^_]+)[^#]*(#video=([^_&]+))?", frame:"<iframe allowfullscreen frameborder='0' src = '//www.dailymotion.com/embed/video/" + match + "' width='640' height='360'></iframe>"})
    #youku
    parametrosVideo.append({url: link, indice:1, regExp:r"\/\/v\.youku\.com\/v_show\/id_(\w+)=*\.html", frame:"<iframe webkitallowfullscreen mozallowfullscreen allowfullscreen frameborder='0' src='//player.youku.com/embed/" + match + "' height='498' width='510'></iframe>"})
    #.mp4, .ogg, .webm
    parametrosVideo.append({url: link, indice:0, regExp:r"^.+.(mp4|m4v|ogg|ogv|webm)$", frame:"<video controls src='" + match + "' width='640' height='360'></video>"})
    #default
    parametrosVideo.append({url: link, indice:0, regExp:link, frame:"<iframe allowfullscreen src='" + match + "'></iframe>"})
    
    encontrado = False
    i = 0
    while encontrado is False and i < len(parametrosVideo):
        parametro = parametrosVideo[i]
        htmlGenerado = traerFrameVideo(parametro[url], parametro[regExp], parametro[indice], parametro[frame])
        if htmlGenerado is not None:
            encontrado = True
        
        i+=1    
        
    return htmlGenerado
    
def traerFrameVideo(url, regExp, indice, frame):
    import re
    busqueda = re.search(regExp, url)
    match = None
    frameVideo = None
    
    if busqueda is not None:
        match = busqueda.group(indice)
    
    if match is not None and len(match) > 0:
        frameVideo = frame.replace("{match}", match)
    
    return frameVideo
