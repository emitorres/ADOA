from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from Adoa2app.models import Usuario, TipoUsuario, Menu, MenuTipoUsuario
from Adoa2app.usuario.forms import UsuarioForm, TipoUsuarioForm,MenuForm,MenuTipoUsuarioForm
from django.forms.widgets import CheckboxSelectMultiple
from Adoa2app.usuario.access import my_access_required

@my_access_required
def index_administrador(request):
	return render_to_response('administrador/AdministradorBase.html', locals(), context_instance = RequestContext(request))

@my_access_required
def usuarios_index(request):
	lista = Usuario.objects.all()
	return render_to_response('administrador/ListaUsuarios.html', locals(), context_instance = RequestContext(request))
        
@my_access_required
def usuarios_edit(request, registro):
	# formulario - msg_no - ver_error - lista_err: se deben llamar asi, el include las referencian con ese nombre
	
	valido = False
	ver_error = False
	msg_ok = 'Operacion Exitosa'
	#msg_no = 'No se pudo realizar la operacion'
	lista_err = []
	
	try:
		usuario = Usuario.objects.get(id = registro)
	except:
		usuario = Usuario()

	if request.method == 'POST':
		formulario = UsuarioForm(request.POST, instance = usuario)

		
		valido = formulario.is_valid()
		if valido:
			formulario.save()
			ver_error = True
			lista_err.append(('','Guardado con exito!'))
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append((field.auto_id,field.label + ': ' + error))
	else:
		formulario = UsuarioForm(instance = usuario)

	# locals() es un diccionario con todas las variables locales y sus valores
	return render_to_response('administrador/edit.html', locals(), context_instance = RequestContext(request))


@my_access_required
def perfiles_index(request):
	lista = TipoUsuario.objects.all()
	return render_to_response('administrador/perfil/ListaPerfiles.html', locals(), context_instance = RequestContext(request))

@my_access_required
def perfiles_edit(request, registro):
	# formulario - msg_no - ver_error - lista_err: se deben llamar asi, el include las referencian con ese nombre
	valido = False
	ver_error = False
	msg_ok = 'Operacion Exitosa'
	#msg_no = 'No se pudo realizar la operacion'
	lista_err = []

	try:
		tusuario = TipoUsuario.objects.get(id = registro)
	except:
		tusuario = TipoUsuario()

	if request.method == 'POST':
		formulario = TipoUsuarioForm(request.POST, instance = tusuario)
		valido = formulario.is_valid()
		if valido:
			ver_error = True
			lista_err.append(('','Guardado con exito!'))
			formulario.save()
			nombre = formulario.cleaned_data['nombre']
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append((field.auto_id,field.label + ': ' + error))
	else:
		formulario = TipoUsuarioForm(instance = tusuario)

	# locals() es un diccionario con todas las variables locales y sus valores
	return render_to_response('administrador/perfil/edit.html', locals(), context_instance = RequestContext(request))

def menu_index(request):
	lista = Menu.objects.all()
	return render_to_response('administrador/menu/ListaMenus.html', locals(), context_instance = RequestContext(request))

def menu_edit(request, registro):
	# formulario - msg_no - ver_error - lista_err: se deben llamar asi, el include las referencian con ese nombre
	valido = False
	ver_error = False
	msg_ok = 'Operacion Exitosa'
	#msg_no = 'No se pudo realizar la operacion'
	lista_err = []

	# Redefine el campo ManyToMany (por defecto lista multiple) a lista de checkbox
	
	MenuForm.base_fields['tipousuarios'].widget = CheckboxSelectMultiple(attrs={'type':'checkbox','class':'filled-in','id':'filled-in-box'},choices=MenuForm.base_fields['tipousuarios'].choices)
	try:
		menu = Menu.objects.get(id = registro)
	except:
		menu = Menu()

	if request.method == 'POST':
		formulario = MenuForm(request.POST, instance = menu)
		valido = formulario.is_valid()
		if valido:
			formulario.save()
			nombre = formulario.cleaned_data['nombre']
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append((field.auto_id,field.label + ': ' + error))
	else:
		formulario = MenuForm(instance = menu)

	# locals() es un diccionario con todas las variables locales y sus valores
	return render_to_response('administrador/menu/edit.html', locals(), context_instance = RequestContext(request))	
def eliminar_acceso(request, registro):
	acceso = MenuTipoUsuario.objects.get(id = registro)
	valido = False
	ver_error = False
	lista_err = []

	if acceso:
		
		ver_error = True
		lista_err.append(('','Acceso Eliminado'))
		acceso.delete()
		return redirect('administrador:administrador_permisos_index')

	return render_to_response('administrador/MenuUsuario/ListaMenuUsuario.html', locals(), context_instance = RequestContext(request))	

def menu_tipo_index(request):
	lista = MenuTipoUsuario.objects.all()
	return render_to_response('administrador/MenuUsuario/ListaMenuUsuario.html', locals(), context_instance = RequestContext(request))

def menu_tipo_edit(request, registro):
	# formulario - msg_no - ver_error - lista_err: se deben llamar asi, el include las referencian con ese nombre
	valido = False
	ver_error = False
	msg_ok = 'Operacion Exitosa'
	#msg_no = 'No se pudo realizar la operacion'
	lista_err = []

	try:
		acc = MenuTipoUsuario.objects.get(id = registro)
	except:
		acc = MenuTipoUsuario()

	if request.method == 'POST':

		formulario = MenuTipoUsuarioForm(request.POST, instance = acc)
		valido = formulario.is_valid()
		if valido:
			
			menu = formulario.cleaned_data['menu']
			tipo = formulario.cleaned_data['tipousuario']

			oatipo = TipoUsuario.objects.get(id = tipo.id)
			oamenu = Menu.objects.get(id = menu.id)

			usrLog = MenuTipoUsuario.objects.emi(oamenu, oatipo)

			if usrLog == None:
				formulario.save()
				ver_error = True
				lista_err.append(('','Guardado con exito!'))
			else:
				ver_error = True
				lista_err.append(('','Este control ya se encuentra establecido'))

			#nombre = str(formulario.cleaned_data['tipousuario']) + ' - ' + str(formulario.cleaned_data['menu'])
		else:
			ver_error = True
			# Arma una lista con errores
			for field in formulario:
				for error in field.errors:
					lista_err.append((field.auto_id,field.label + ': ' + error))
	else:
		formulario = MenuTipoUsuarioForm(instance = acc)
		

	# locals() es un diccionario con todas las variables locales y sus valores
	return render_to_response('administrador/MenuUsuario/edit.html', locals(), context_instance = RequestContext(request))
"""

def menu_tipo_edit(request,registro):
	listaMenu = Menu.objects.all()
	listaTipo = TipoUsuario.objects.all()
	if request.method == 'POST':

		menu = request.POST['menu']
		tipo = request.POST['tipo']

		oatipo = TipoUsuario.objects.get(id = tipo.id)
		oamenu = Menu.objects.get(id = menu.id)

		usrLog = MenuTipoUsuario.objects.emi(oamenu.id, oatipo.id)
		if usrLog != None:
			#b = MenuTipoUsuario.objects.get(tipousuario_id = oatipo.id)
			#if b != None:
			oa = MenuTipoUsuario(menu = oamenu, tipousuario = oatipo)
			oa.save()	
	return render_to_response('administrador/MenuUsuario/edit.html', locals(), context_instance = RequestContext(request))

     """