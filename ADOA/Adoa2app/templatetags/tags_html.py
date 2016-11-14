from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
import datetime
from Adoa2app.models import Usuario, Menu

register = template.Library()

# ---------- Ver la informacion del pie de pagina ----------
@register.simple_tag
def info_del_pie(request):
	if 'usuario' in request.session: usuario = request.session['usuario'].nombre
	else: usuario = ''
	now = datetime.datetime.now()
	if usuario != '': usuario = usuario + ' - '
	cadena = usuario + now.strftime("%d/%m/%Y - %H:%M") + ' - Todos los derechos reservados 2012'
	return '%s' % (cadena)

@register.simple_tag
def info_usuario(request):
	if 'usuario' in request.session: usuario = request.session['usuario'].nombre
	else: usuario = ''
	if usuario != '': usuario = usuario
	cadena = usuario 
	return '%s' % (cadena)

@register.simple_tag
def traer_usuario(request):
	if 'usuario' in request.session:
		idusuario = request.session['usuario'].id
		usuario = Usuario.objects.all()

		for user in usuario:
			if user.id == idusuario:
				userfinal = user.nombre+' '+user.apellido
				return '%s' % userfinal
	else: usuario = ''
	if usuario != '': usuario = usuario
	cadena = ''
	return '%s' % (cadena)


# ---------- Referencias de la libreria static ----------

@register.simple_tag
def css_tag(css):
	return '%s%s%s' % (settings.STATIC_URL , 'stylesheets/' , css)

@register.inclusion_tag('tags/img.html')
def image_tag(img):
	return { 'imagen' : '%s%s%s' % (settings.STATIC_URL , 'images/' , img) }

# ---------- Link a cadenas o imagenes ----------

@register.inclusion_tag('tags/url.html')
def url_tag(title, link):
	link_to = reverse(link) # Del nombre del link se obtiene la url
	return { 'title' : title, 'link_to' : link_to, }

@register.inclusion_tag('tags/url_img.html')
def url_img_tag(img, link):
	imagen = '%s%s%s' % (settings.STATIC_URL , 'images/' , img)
	link_to = reverse(link) # Del nombre del link se obtiene la url
	return { 'imagen' : imagen, 'link_to' : link_to, }

@register.inclusion_tag('tags/url_button.html')
def url_button(title, link):
	link_to = reverse(link) # Del nombre del link se obtiene la url
	return { 'title' : title, 'link_to' : link_to, }


# ---------- Carga de menu izquierdo ----------

@register.inclusion_tag('tags/url.html')
def menu_tag(request, title, link):
	link_to = reverse(link) # Del nombre del link se obtiene la url
	is_log = 'usuario' in request.session
	if (title == 'Ingreso'):
		if is_log: return None
	else:
		if is_log == False: return None
	return { 'title' : title, 'link_to' : link_to, }

# ---------- Aplica un filtro en los campos de fecha ----------

@register.filter
def filtro_fecha(fecha):
	return fecha.strftime("%d/%m/%Y - %H:%M")
# Modo de llamado {{ alguna_variable_a_filtrar|filtro_fecha }}

@register.inclusion_tag('tags/menu_sist.html')
def menu_sist_tag(request):
	is_log = 'usuario' in request.session
	if is_log == False: return None

	lista = Menu.objects.todos()

	for registro in lista: 
		imagen = 'icono_menu.gif'
		if registro.icono != '': imagen = registro.icono
		registro.icono = '%s%s%s' % (settings.STATIC_URL , 'images/', imagen)
		if registro.action != '':
			registro.url = reverse(registro.action)
	return { 'lista' : lista, }