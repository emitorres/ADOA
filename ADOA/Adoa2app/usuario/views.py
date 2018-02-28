# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from Adoa2app.usuario.forms import CambioPerfilForm, RegistroForm, IngresoForm,PerfilForm,PerfilIndexForm, RecuperarContrasenaForm,CambioPwdForm,CambioPwdForm2
from Adoa2app.models import Usuario, TipoUsuario, Token
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from Adoa2app.usuario.access import my_login_required,my_access_required
from django.conf import settings
from passlib.hash import django_pbkdf2_sha256 as handler
from passlib.hash import pbkdf2_sha256
import uuid
import sys
import json

reload(sys)


def index_usuarioBase(request):
	id = request.session['usuario'].id
	usuario = Usuario.objects.get(id= id)
	return render_to_response('usuario/ConfiguracionBase.html', locals(), context_instance = RequestContext(request))

def usuario_index(request):
	return render_to_response('usuario/InicioSesion.html', locals(), context_instance = RequestContext(request))

def registro(request):
	valido = False
	ver_error = False
	msg_ok = 'Operación Exitosa'
	msg_no = 'No se pudo realizar la operación'
	lista_err = []

	try:
		usuario = Usuario.objects.get(id = registro)
	except:
		usuario = Usuario()

	if request.method == 'POST':
		formulario = RegistroForm(request.POST, instance = usuario)
		valido = formulario.is_valid()
		if valido:
			user = formulario.save(commit=False)
			user.clave = Usuario.objects.encriptarPass(user.dni)
			user.estado = False
			if user.sexo == 1:
				user.sexo = 1
			else:
				user.sexo = 0

			user.save()
			usuario = formulario.cleaned_data['email']
			usuario1 = Usuario.objects.get(email = usuario)

			token1 = Token()
			token1.token = uuid.uuid4()
			token1.usuario = usuario1
		
			token1.save()
			usuarioMail = formulario.cleaned_data['email']
			#clave = formulario.cleaned_data['clave']
			usrLog = Usuario.objects.email_ok(usuarioMail)
			if usrLog != None:
				subject = 'Verificación de Email'

				fromUsuario = settings.EMAIL_HOST_USER 
				to = Token.objects.get(usuario_id = usrLog.id)
				toMail = [usrLog.email]
				message = u'Hola %s %s, bienvenido a ADOA 2.0, por favor haga click en el siguiente enlace para confirmar su e-mail: %s/usuario/confirmar_cuenta/%s\n\nUsuario: %s\nContraseña: %s' %(usrLog.nombre, usrLog.apellido, traerUrlBase(request), str(to.token), usrLog.email, usrLog.dni)
				#message = 'Hola ' +usrLog.nombre +' '+usrLog.apellido + ', bienvenido a ADOA 2.0 por favor haga click en el siguiente enlace para confirmar su email '+ traerUrlBase(request) + '/usuario/confirmar_cuenta/'+str(to.token) + '\n\n' + 'Usuario: ' + usrLog.email + '\n'+ 'Contraseña: '+ usrLog.dni
				mail = EmailMessage(subject, message,fromUsuario,toMail)
				mail.send()
			#formulario.save()
			#return redirect('usuario:usuario_informacion_registro')
			nombre = formulario.cleaned_data['nombre']
		else:
			ver_error = True
			campo = {}
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append((field.auto_id, field.label + ': ' + error))
					
	else:
		formulario = RegistroForm(instance = usuario)
	# locals() es un diccionario con todas las variables locales y sus valores
	return render_to_response('usuario/Registro.html', locals(), context_instance = RequestContext(request))

def cambioPerfil(request):

	id = request.session['usuario'].id
	usuario = Usuario.objects.get(id= id)
	valido = False
	ver_error = False
	msg_no  = 'Ingreso no valido'
	lista_err = []
	lista_ok = []
	if request.method == 'POST':
		formulario = CambioPerfilForm(request.POST)
		valido = formulario.is_valid()
		if valido:
			razones = formulario.cleaned_data['razones']
			subject = 'Cambio Perfil'
			toMail = [settings.EMAIL_HOST_USER]
			fromMail = usuario.email
			message = 'El usuario '+ usuario.nombre +' ' + usuario.apellido+ ' solicito cambio de perfil.' + '\n\n'+ 'Razones: '+'\n\n'+razones
			mail = EmailMessage(subject, message, fromMail, toMail)
			ver_ok = True if mail.send() > 0 else False

			if ver_ok is True:
				lista_ok.append('Email enviado correctamente. En breve sera atendida su solicitud')
			else:
				lista_err.append(('', 'No se pudo enviar el mail de recuperacion. Por favor, intente mas tarde'))	
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append((field.auto_id, field.label + ': ' + error))
	else:
		formulario = CambioPerfilForm()

	return render_to_response('usuario/CambioPerfil.html', locals(), context_instance = RequestContext(request))

def iniciarSesion(request):
	valido = False
	ver_error = False
	msg_no  = 'Ingreso no valido'
	lista_err = []
	if request.method == 'POST':
		formulario = IngresoForm(request.POST)
		valido = formulario.is_valid()
		if valido:
			usuario = formulario.cleaned_data['usuario']
			clave = formulario.cleaned_data['clave']
			#usrLog = Usuario.objects.login_ok(usuario, clave)
			usrLog = Usuario.objects.validarPass(usuario, clave)
			if usrLog != None:
				request.session['usuario'] = usrLog
				if request.session['usuario'].tipousuario.id == 1:
					return redirect('administrador:index_administrador')
				if request.session['usuario'].tipousuario.id == 2:
					return redirect('/Inicio/1')
				if request.session['usuario'].tipousuario.id == 3:
					return redirect('/Objetos/2')
			else:
				ver_error = True
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append((field.auto_id, field.label + ': ' + error))
	else:
		formulario = IngresoForm()

	return render_to_response('usuario/InicioSesion.html', locals(), context_instance = RequestContext(request))
@my_login_required
def perfil_index(request):

	id = request.session['usuario'].id
	usuario = Usuario.objects.get(id= id)

	
	return render_to_response('usuario/ConfiguracionBase.html', locals(), context_instance = RequestContext(request))	
	
@my_login_required
def perfil_editar(request,registro):
	id = request.session['usuario'].id
	usuario = Usuario.objects.get(id= id)

	valido = False
	ver_error = False
	msg_ok = 'Operacion Exitosa'
	msg_no = 'No se pudo realizar la operacion'
	lista_err = []

	try:
		usuario = Usuario.objects.get(id = registro)
	except:
		usuario = Usuario()

	if request.method == 'POST':
		formulario = PerfilForm(request.POST, instance = usuario)
		valido = formulario.is_valid()
		if valido:
			formulario.save()
			return redirect('usuario:index_usuarioBase')
			#nombre = formulario.cleaned_data['nombre']
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append((field.auto_id,field.label + ': ' + error))
	else:
		formulario = PerfilForm(instance = usuario)
	# locals() es un diccionario con todas las variables locales y sus valores
	return render_to_response('usuario/EditarPerfil.html', locals(), context_instance = RequestContext(request))
@my_login_required
def usuario_salir(request):
	del request.session['usuario']
	return HttpResponseRedirect('/')

def usuario_acceso_denegado(request):
	return render_to_response('usuario/acceso_denegado.html', locals(), context_instance = RequestContext(request))

def informacion_registro(request):
	return render_to_response('usuario/InformacionRegistro.html', locals(), context_instance = RequestContext(request))


def recuperar_contrasena(request):
	valido = False
	ver_error = False
	ver_ok = False
	msg_no  = 'Ingreso no valido'
	lista_err = []
	lista_ok = []
	if request.method == 'POST':
		formulario = RecuperarContrasenaForm(request.POST)
		valido = formulario.is_valid()
		if valido:	
			usuarioMail = formulario.data['email']
			usuario1 = Usuario.objects.get(email = usuarioMail)

			tokenCadena = uuid.uuid4()
			token1 = Token(1,tokenCadena, usuario1.id)

			token1.save()
			#clave = formulario.cleaned_data['clave']
			usrLog = Usuario.objects.email_ok(usuarioMail)
			if usrLog != None:
				subject = 'Recuperar Contrasena'

				toMail = [usrLog.email]
				toToken = Token.objects.get(usuario_id = usrLog.id)
				fromMail = settings.EMAIL_HOST_USER
				message = traerUrlBase(request)+'/usuario/recuperar/cambio_clave/'+str(toToken.token)
				mail = EmailMessage(subject, message, fromMail, toMail)
				ver_ok = True if mail.send() > 0 else False

				if ver_ok is True:
					lista_ok.append('Email enviado correctamente. Revise su correo electronico')
				else:
					lista_err.append(('', 'No se pudo enviar el mail de recuperacion. Por favor, intente mas tarde'))
				
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append((field.auto_id,field.label + ': ' + error))
	else:
		formulario = RecuperarContrasenaForm()

	return render_to_response('usuario/RecuperarContrasena.html', locals(), context_instance = RequestContext(request))


def cambiar_clave(request,registro):
	# formulario - msg_no - ver_error - lista_err: se deben llamar asi, el include las referencian con ese nombre
	


	valido = False
	ver_error = False
	msg_no = 'Cambio de clave no valido'
	lista_err = []
	"""
	try:
		usuario = Usuario.objects.get(id = registro)
	except:
		usuario = Usuario()
	"""

	token2 = Token.objects.all()

	if token2:
		token1 = Token.objects.get(token = registro)
		usuario = Usuario.objects.get(id = token1.usuario_id)
		emailuser = usuario.email


		if request.method == 'POST':
			formulario = CambioPwdForm(request.POST)
			valido = formulario.is_valid()
			if valido:
				nueva = formulario.cleaned_data['nueva']
				repetida = formulario.cleaned_data['repetida']

				cambio = Usuario.objects.cambiar_clave2(usuario.id, nueva)

				if cambio: 
					token1.delete()

					#return HttpResponseRedirect('/adoa/')
				else: ver_error = True
			else:
				ver_error = True
				# Arma una lista con errores
				for field in formulario:
					for error in field.errors:
						lista_err.append((field.auto_id,field.label + ': ' + error))
		else:
			formulario = CambioPwdForm()
	else:
		return render_to_response('usuario/acceso_denegado.html', locals(), context_instance = RequestContext(request))			
	return render_to_response('usuario/cambio_clave_mail.html', locals(), context_instance = RequestContext(request))


@my_login_required
def cambio_clave(request,registro):
	# formulario - msg_no - ver_error - lista_err: se deben llamar asi, el include las referencian con ese nombre
	usuario = request.session['usuario'].id

	valido = False
	ver_error = False
	msg_no = 'Cambio de clave no valido'
	lista_err = []
	try:
		usuario = Usuario.objects.get(id = registro)
	except:
		usuario = Usuario()
	if request.method == 'POST':
		formulario = CambioPwdForm2(request.POST)
		valido = formulario.is_valid()
		if valido:
			actual = formulario.cleaned_data['actual']
			nueva = formulario.cleaned_data['nueva']
			repetida = formulario.cleaned_data['repetida']

			cambio = Usuario.objects.cambiar_clave(usuario.id, actual, nueva)

			if cambio: return HttpResponseRedirect('/usuario/configuracion/')
			else: ver_error = True
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append((field.auto_id,field.label + ': ' + error))
	else:
		formulario = CambioPwdForm2()
	v = locals()
	v['id'] = registro
	v['formulario'] = formulario
	#return render_to_response('usuario/cambio_clave.html', locals(), context_instance = RequestContext(request))
	return render(request, 'usuario/cambio_clave.html', v)

def confirmar_cuenta(request,registro):
	token2 = Token.objects.all()
	if token2:
		token1 = Token.objects.get(token = registro)
		usuario = Usuario.objects.get(id = token1.usuario_id)
		emailuser = usuario.email
		usuario.estado = True
				
		#Si es email de institución educativa, el rol es de docente editor	
		expresion_regular = r"(\@edu\.)|(\@.*\.edu\.)"
		if evaluar(expresion_regular,emailuser):
			usuario.tipousuario = TipoUsuario.objects.get(id = 2)
		else: #no es de educativo, rol docente 'común'	
			usuario.tipousuario = TipoUsuario.objects.get(id = 3)
		usuario.save()
		token1.delete()
		
		return render_to_response('usuario/ConfirmarCuenta.html', locals(), context_instance = RequestContext(request))
	else:
		return render_to_response('usuario/acceso_denegado.html', locals(), context_instance = RequestContext(request))			
	

def evaluar(exp, cad): 
	import re 
	if re.search(exp, cad, re.IGNORECASE) is None:
		return False
	else:
		return True


def confirmar_cuenta2(request):

	return render_to_response('usuario/ConfirmarCuenta.html', locals(), context_instance = RequestContext(request))
	
	
def eliminar_usuario(request, registro):
	usuario = Usuario.objects.get(id = registro)
	valido = False
	ver_error = False
	lista_err = []

	if usuario:
		
		ver_error = True
		lista_err.append(('','Usuario Eliminado'))
		usuario.delete()
		return redirect('administrador:administrador_usuarios_index')

	return render_to_response('administrador/ListaUsuarios.html', locals(), context_instance = RequestContext(request))	
	#return HttpResponseRedirect('/administrador/usuarios')
	

def traerUrlBase(request):
	dominio = request.get_host()
	protocolo = 'https://' if request.is_secure() else 'http://'
	return protocolo + dominio

