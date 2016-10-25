from django import forms
from Adoa2app.usuario.models import Usuario, TipoUsuario, Menu, MenuTipoUsuario
from passlib.hash import django_pbkdf2_sha256 as handler

class RegistroForm(forms.ModelForm):
	class Meta:
			model = Usuario
			def save(self):
			    # Sets username to email before saving
			    user = super(RegistroForm, self).save(commit=False)
			    user.nombre = user.dni
			    user.save()
			    return user	


			fields = [
				'nombre',
				'apellido',
				'dni',
				'carrera',
				'email',
			]

			labels = {
				'nombre':'Nombre',
				'apellido':'Apellido',
				'dni':'DNI',
				'carrera':'Carrera',
				'email':'Email',
			}

			widgets = {
				'nombre':forms.TextInput(),
				'apellido':forms.TextInput(),
				'dni':forms.TextInput(),
				'carrera':forms.TextInput(),
				'email':forms.TextInput(),
			}
	def clean_nombre(self):
		nombre = self.cleaned_data.get('nombre')
		if len(nombre) < 3:
			raise forms.ValidationError('El nombre debe tener mas de 3 caracteres')
		return nombre
		"""
	def clean_dni(self):
		dni = self.cleaned_data.get('dni')
		if len(dni) != 8:
			raise forms.ValidationError('El dni debe tener de 8 caracteres')
		return dni	
"""

	def clean_dni(self):
		dni = self.cleaned_data.get("dni")
		punto = dni.split(".")
		if punto == ".":
			raise forms.ValidationError('El dni no debe tener puntos')
		return dni	
		
class IngresoForm(forms.Form):
	class Meta:
			model = Usuario

	usuario = forms.CharField(error_messages = {'required': 'Debe ingresar un usuario'})
	clave   = forms.CharField(widget = forms.PasswordInput(),
							  error_messages = {'required': 'Debe ingresar una clave'})	
	def clean_usuario(self):
		"""
		email = self.cleaned_data.get('usuario')
		existe = Usuario.objects.all()
		for user in existe:
			if user.email != email:
				raise forms.ValidationError('No existe ningun usuario registrado con ese correo electronico.')
			else:
				return email				
		"""
		try:
			email = self.cleaned_data.get('usuario')
			existe = Usuario.objects.get(email = email)
		except Usuario.DoesNotExist:
			raise forms.ValidationError('No existe ningun usuario registrado con ese correo electronico.')
		else:
			return email	

class CambioPwdForm(forms.Form):
	
	nueva = forms.CharField(widget = forms.PasswordInput(),
							error_messages = {'required': 'Debe ingresar la clave nueva'})
	repetida = forms.CharField(widget = forms.PasswordInput(),
							   error_messages = {'required': 'Debe ingresar la clave repetida'})
	

	fields = [
		'nueva',
		'repetida',
	]

	labels = {
		'nueva':'Nueva',
		'repetida':'Repetida',
		
	}


	# Las validaciones para campos son clean_<nombre_campo>
	# Si el metodo se llama clean es para todos los campos juntos
	#validaciones propias
	def clean_repetida(self):
		nueva = self.cleaned_data.get('nueva')
		repetida = self.cleaned_data.get('repetida')
		#if nueva != repetida:
		n = handler.encrypt(nueva)
		r = handler.encrypt(repetida)

		h = handler.verify(repetida, n)
		if not h:
			raise forms.ValidationError('Clave nueva y repetida deben ser iguales')
		return repetida		


class CambioPwdForm2(forms.Form):
	actual = forms.CharField(widget = forms.PasswordInput(),
							 error_messages = {'required': 'Debe ingresar la clave actual'})
	nueva = forms.CharField(widget = forms.PasswordInput(),
							error_messages = {'required': 'Debe ingresar la clave nueva'})
	repetida = forms.CharField(widget = forms.PasswordInput(),
							   error_messages = {'required': 'Debe ingresar la clave repetida'})
	

	

	
	fields = [
		'actual',
		'nueva',
		'repetida',
	]

	labels = {
		'actual':'Actual',
		'nueva':'Nueva',
		'repetida':'Repetida',
		
	}


	# Las validaciones para campos son clean_<nombre_campo>
	# Si el metodo se llama clean es para todos los campos juntos
	#validaciones propias
	def clean_repetida(self):
		nueva = self.cleaned_data.get('nueva')
		repetida = self.cleaned_data.get('repetida')
		#if nueva != repetida:
		n = handler.encrypt(nueva)
		r = handler.encrypt(repetida)

		h = handler.verify(repetida, n)
		if not h:
			raise forms.ValidationError('Clave nueva y repetida deben ser iguales')
		return repetida		


class PerfilForm(forms.ModelForm):
	class Meta:
			model = Usuario

			fields = [
				'nombre',
				'apellido',
				'dni',
				'carrera',
			]

			labels = {
				'nombre':'Nombre',
				'apellido':'Apellido',
				'dni':'DNI',
				'carrera':'Carrera',
			}

			widgets = {
				'nombre':forms.TextInput(),
				'apellido':forms.TextInput(),
				'dni':forms.TextInput(),
				'carrera':forms.TextInput(),
			}


class PerfilIndexForm(forms.ModelForm):
	class Meta:
			model = Usuario

class RecuperarContrasenaForm(forms.ModelForm):
	class Meta:
			model = Usuario

			fields = [
				'email',
			]
			#'tipousuario':forms.CheckboxInput(attrs={'class':'filled-in'}),

			labels = {
				'email':'Email',
			}

			widgets = {

				'email':forms.TextInput(),
			}
	def clean_email(self):
		email = self.cleaned_data.get('email')
		try:
			Usuario.objects.get(email = email);
		except:
			raise forms.ValidationError('No existe ningun usuario registrado con ese correo electronico. Por favor verifique su mail y vuelva a intentarlo')
		return email	

class TipoUsuarioForm(forms.ModelForm):
	class Meta:
		model = TipoUsuario
		
	def clean_nombre(self):
		nombre = self.cleaned_data.get('nombre')
		if len(nombre) < 3:
			raise forms.ValidationError('El nombre debe tener mas de 3 caracteres')
		return nombre

class MenuForm(forms.ModelForm):
	class Meta:
		model = Menu

		fields = [
			'nombre',
			'tipousuarios',
			'url',

		]

		labels = {
			'nombre':'Nombre',
			'tipousuarios':'Tipousuario',
			'url':'Url',


		}
	
		widgets = {
			'nombre':forms.TextInput(),
			'tipousuarios':forms.Select(attrs={'class':'browser-default'}),
			'url':forms.TextInput(),
		}





		
		
class MenuTipoUsuarioForm(forms.ModelForm):
	class Meta:
		model = MenuTipoUsuario
		fields = {

			'tipousuario',
			'menu',

		}

		labels = {
			'tipousuario':'Tipo usuario',
			'menu':'Menu',


		}
		widgets = {
			
			'tipousuario':forms.Select(attrs={'class':'browser-default'}),
			'menu':forms.Select(attrs={'class':'browser-default'}),
		}

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario# el formaulario por defecto es extender los datos que tiene el usuario

		fields = {

			'tipousuario',

		}

		labels = {
			'tipousuario':'Tipo usuario',


		}
		widgets = {
			
			'tipousuario':forms.Select(attrs={'class':'browser-default'}),
		}



