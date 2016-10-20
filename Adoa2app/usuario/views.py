from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from Adoa2app.usuario.forms import RegistroForm, IngresoForm,PerfilForm,PerfilIndexForm, RecuperarContrasenaForm,CambioPwdForm,CambioPwdForm2
from Adoa2app.usuario.models import Usuario, TipoUsuario,token
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from Adoa2app.usuario.access import my_login_required,my_access_required
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256 as handler



from passlib.hash import pbkdf2_sha256
import uuid
def usuario_index(request):
	return render_to_response('usuario/InicioSesion.html', locals(), context_instance = RequestContext(request))

def registro(request):
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
		formulario = RegistroForm(request.POST, instance = usuario)
		valido = formulario.is_valid()
		if valido:
			user = formulario.save(commit=False)
			
			#enc = pbkdf2_sha256.encrypt(user.dni, rounds=10,salt_size=32)
			
			#user.clave = Usuario.objects.encriptar(user.dni)

			user.clave = Usuario.objects.encriptarPass(user.dni)
			user.estado = False
			"""	
			email = formulario.cleaned_data.get("email")
			email_base, proveedor = email.split("@")
			dominio, extension = proveedor.split(".")
			if extension == "edu":
				user.tipousuario = TipoUsuario.objects.get(id = 1)

				user.save()
			else:	
					"""
			

			user.save()
			usuario = formulario.cleaned_data['email']
			usuario1 = Usuario.objects.get(email = usuario)

			tokenCadena = uuid.uuid4()
			token1 = token(1,tokenCadena, usuario1.id)

		
			token1.save()
			usuarioMail = formulario.cleaned_data['email']
			#clave = formulario.cleaned_data['clave']
			usrLog = Usuario.objects.email_ok(usuarioMail)
			if usrLog != None:
				subject = 'Verificacion de Email'

				fromUsuario ='adoa2.unla@gmail.com' 
				to = token.objects.get(usuario_id = usrLog.id)
				fromMail = [usrLog.email]

				message = 'Hola ' +usrLog.nombre +' '+usrLog.apellido + ', bienvenido a ADOA 2.0 por favor haga click en el siguiente enlace para confirmar su email '+ 'http://127.0.0.1:8000/usuario/confirmar_cuenta/'+str(to.token) + '\n\n' + 'Usuario: ' + usrLog.email + '\n'+ 'Contrasena: '+ usrLog.dni
				mail = EmailMessage(subject, message,fromUsuario,fromMail)
				mail.send()
			#formulario.save()
			#return redirect('usuario:usuario_informacion_registro')
			nombre = formulario.cleaned_data['nombre']
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append(field.label + ': ' + error)
	else:
		formulario = RegistroForm(instance = usuario)
	# locals() es un diccionario con todas las variables locales y sus valores
	return render_to_response('usuario/Registro.html', locals(), context_instance = RequestContext(request))

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
				else:
					return redirect('CrearOA')
			else:
				ver_error = True
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append(field.label + ': ' + error)
	else:
		formulario = IngresoForm()

	return render_to_response('usuario/InicioSesion.html', locals(), context_instance = RequestContext(request))
@my_login_required
def perfil_index(request):

	id = request.session['usuario'].id
	usuario = Usuario.objects.get(id= id)

	
	return render_to_response('usuario/Perfil.html', locals(), context_instance = RequestContext(request))	
	
@my_login_required
def perfil_editar(request,registro):
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
			return redirect('usuario:perfil_index')
			#nombre = formulario.cleaned_data['nombre']
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append(field.label + ': ' + error)
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

			

			usuarioMail = formulario.cleaned_data['email']


			usuario1 = Usuario.objects.get(email = usuarioMail)

			tokenCadena = uuid.uuid4()
			token1 = token(1,tokenCadena, usuario1.id)

			token1.save()
			#clave = formulario.cleaned_data['clave']
			usrLog = Usuario.objects.email_ok(usuarioMail)
			if usrLog != None:
				subject = 'Recuperar Contrasena'

				sender = usrLog.email
				to = token.objects.get(usuario_id = usrLog.id)
				recipients = ['emitorres93@gmail.com']

				message = 'shttp://127.0.0.1:8000/usuario/recuperar/cambio_clave/'+str(to.token)
				mail = EmailMessage(subject, message, sender,recipients)
				mail.send()

				ver_ok = True
				lista_ok.append('Email enviado correctamente. Revise su correo electronico')
				
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append(field.label + ': ' + error)
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

	token2 = token.objects.all()

	if token2:
		token1 = token.objects.get(token = registro)
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
						lista_err.append(field.label + ': ' + error)
		else:
			formulario = CambioPwdForm()
	else:
		return render_to_response('usuario/acceso_denegado.html', locals(), context_instance = RequestContext(request))			
	return render_to_response('usuario/cambio_clave_mail.html', locals(), context_instance = RequestContext(request))
@my_login_required
def cambio_clave(request,registro):
	# formulario - msg_no - ver_error - lista_err: se deben llamar asi, el include las referencian con ese nombre


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

			if cambio: return HttpResponseRedirect('/adoa/')
			else: ver_error = True
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append(field.label + ': ' + error)
	else:
		formulario = CambioPwdForm2()

	return render_to_response('usuario/cambio_clave.html', locals(), context_instance = RequestContext(request))






def confirmar_cuenta(request,registro):

	token2 = token.objects.all()

	if token2:
		token1 = token.objects.get(token = registro)
		usuario = Usuario.objects.get(id = token1.usuario_id)
		emailuser = usuario.email
		email_base, proveedor = emailuser.split("@")
		dominio, extension = proveedor.split(".")
		if extension == "com":
			usuario.tipousuario = TipoUsuario.objects.get(id = 3)
			#usuario.clave = '456123'
			usuario.estado = True
			usuario.save()
			token1.delete()

		if extension == "edu":
			usuario.tipousuario = TipoUsuario.objects.get(id = 2)
			#usuario.clave = '456123'
			usuario.estado = True
			usuario.save()
			token1.delete()
		return render_to_response('usuario/ConfirmarCuenta.html', locals(), context_instance = RequestContext(request))
	else:
		return render_to_response('usuario/acceso_denegado.html', locals(), context_instance = RequestContext(request))			
	
def confirmar_cuenta2(request):

	return render_to_response('usuario/ConfirmarCuenta.html', locals(), context_instance = RequestContext(request))
	
	
def eliminar_usuario(request, registro):
	usuario = Usuario.objects.get(id = registro)
	usuario.delete()
	return HttpResponseRedirect('/adoa/')
