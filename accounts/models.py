from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from datetime import datetime, timedelta
import jwt
from django.conf import settings

class AccountManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
	# Ensure that an email address is set
		if not email:
			raise ValueError('Users must have a valid e-mail address')
		# Ensure that a username is set
		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username')
	
		account = self.model(
			email=self.normalize_email(email),
			username=kwargs.get('username'),
			firstname=kwargs.get('firstname', None),
			lastname=kwargs.get('lastname', None),
		)

		account.set_password(password)
		account.save()

		return account

	def create_superuser(self, email, password=None, **kwargs):
		account = self.create_user(email, password, kwargs)
		account.is_admin = True
		account.save()
		return account


class Account(AbstractBaseUser):
	username = models.CharField(unique=True, max_length=50)
	email = models.EmailField(unique=True)
	firstname = models.CharField(max_length=100, blank=True)
	lastname = models.CharField(max_length=100, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	is_admin = models.BooleanField(default=False)
	objects = AccountManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	@property
	def token(self):
		"""
		Allows us to get a user's token by calling `user.token` instead of
		`user.generate_jwt_token().

		The `@property` decorator above makes this possible. `token` is called
		a "dynamic property".
		"""
		return self._generate_jwt_token()

	def _generate_jwt_token(self):
		"""
		Generates a JSON Web Token that stores this user's ID and has an expiry
		date set to 60 days into the future.
		"""
		dt = datetime.utcnow()+ timedelta(days=60)

		token = jwt.encode({
		    'id': self.pk,
		    'exp': int(dt.strftime('%s'))
		}, settings.SECRET_KEY, algorithm='HS256')

		return token.decode('utf-8')



