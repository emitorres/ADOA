from django.db import models
import hashlib
import uuid
from passlib.hash import django_pbkdf2_sha256 as handler

#--------------------------------------------------------------------------

class TipoUsuarioManager(models.Manager):
# Al heredar de Manager, en model se tiene al modelo actual

	def todos(self):
		return self.model.objects.all()
	
	def traerPorId(self, tuId):
		return self.model.objects.filter(id = tuId)

#---------------------------------------------------------------------------

class UsuarioManager(models.Manager):

	def todos(self):
		return self.model.objects.all()

	def login_ok(self, usuario, clave):
		try:
			existe = self.model.objects.get(email = usuario, clave = clave)
		except self.model.DoesNotExist:
			return None
		else:
			return existe


	def validarPass(self,usuario,clave):

		try:
			existe = self.model.objects.get(email = usuario)
		
		except self.model.DoesNotExist:
			return None
		
		h = handler.verify(clave, existe.clave)

		if h & existe.estado == True:
			return existe
		else:
			return None



	def cambiar_clave(self, id, actual, nueva):
		usuario = self.model.objects.get(id = id)

		h = handler.verify(actual, usuario.clave)


		if not h: return False
		usuario.clave = handler.encrypt(nueva)
		usuario.save()
		return True

	def cambiar_clave2(self, id,nueva):
		usuario = self.model.objects.get(id = id)

		usuario.clave = handler.encrypt(nueva)
		usuario.save()
		return True
		
	def email_ok(self,email):
		try:
			existe = self.model.objects.get(email = email)
		except self.model.DoesNotExist:
			return None
		else:
			return existe

	def encriptar(self,clave):
		salt = uuid.uuid4().hex
		return hashlib.sha256(salt.encode() + clave.encode()).hexdigest() + ':' + salt

	def validar(self, clave , usuario):
		existe = self.model.objects.get(email = usuario)
		password, salt = existe.clave.split(':')
		return password == hashlib.sha256(salt.encode() + clave.encode()).hexdigest()
			

	def check_passwd(self,usuario, clave):
		
	# ... get 'hsh_passwd' from database based on 'user' ...
		user = self.model.objects.get(email = usuario)
		user.clave = user.clave.split(':')
		salt = user.clave[1]
		hsh = user.clave[2]
		if hsh == hashlib.sha1(salt + clave).hexdigest():
			return True
		return False

	def encriptarPass(self, clave):
		return handler.encrypt(clave)


"""
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
"""

#--------------------------------------------------------------------------

class MenuManager(models.Manager):
# Al heredar de Manager, en model se tiene al modelo actual

	def todos(self):
		return self.model.objects.all()

#---------------------------------------------------------------------------

class MenuTipoUsuarioManager(models.Manager):
# Al heredar de Manager, en model se tiene al modelo actual

	def todos(self):
		return self.model.objects.all()

	def emi(self, idmenu, idtipo):
		try:
			existe = self.model.objects.get(menu_id = idmenu.id, tipousuario_id = idtipo.id)
		except self.model.DoesNotExist:
			return None
		else:
			return existe

#---------------------------------------------------------------------------