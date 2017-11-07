from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Account, Profile
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist

class AccountSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True)

	token = serializers.CharField(max_length=255, read_only=True)

	class Meta:
		model = Account
		fields = (
		'id', 'email', 'username', 'date_created', 'date_modified',
		'firstname', 'lastname', 'password', 'confirm_password', 'token' )
		read_only_fields = ('date_created', 'date_modified')

	def create(self, validated_data):
		return Account.objects.create_user(**validated_data)

	def update(self, instance, validated_data):
		instance.email = validated_data.get('email', instance.email)
		instance.username = validated_data.get('username',
		instance.username)
		instance.firstname = validated_data.get('firstname',
		instance.firstname)
		instance.lastname = validated_data.get('lastname',
		instance.lastname)
		password = validated_data.get('password', None)
		confirm_password = validated_data.get('confirm_password', None)
		if password and password == confirm_password:
			instance.set_password(password)
		instance.save()
		return instance

	# def validate(self, data):
	# 	'''
	# 	Ensure the passwords are the same
	# 	'''
	# 	if data['password']:
	# 		if data['password'] != data['confirm_password']:
	# 			raise serializers.ValidationError(
	# 				"The passwords have to be the same"
	# 	)
	# 	return data




class LoginSerializer(serializers.Serializer):
	email = serializers.CharField(max_length=255, read_only=True)
	username = serializers.CharField(max_length=255, required=True)
	password = serializers.CharField(max_length=128, write_only=True, required=True,
		error_messages={"required": "Password field may not be blank."})
	token = serializers.CharField(max_length=255, read_only=True)

	def validate(self, data):
		# The `validate` method is where we make sure that the current
		# instance of `LoginSerializer` has "valid". In the case of logging a
		# user in, this means validating that they've provided an email
		# and password and that this combination matches one of the users in
		# our database.
		username = data.get('username', None)
		password = data.get('password', None)
		user = authenticate(username=username, password=password)

		# If no user was found matching this email/password combination then
		# `authenticate` will return `None`. Raise an exception in this case.
		if user is None:
			raise serializers.ValidationError(
				'A user with this email and password was not found.'
			)

		# Django provides a flag on our `User` model called `is_active`. The
		# purpose of this flag is to tell us whether the user has been banned
		# or deactivated. This will almost never be the case, but
		# it is worth checking. Raise an exception in this case.
		if not user.is_active:
			raise serializers.ValidationError(
				'This user has been deactivated.'
			)

		# The `validate` method should return a dictionary of validated data.
		# This is the data that is passed to the `create` and `update` methods
		# that we will see later on.
		return {
			'email': user.email,
			'username': user.username,
			'token': user.token
		}

class AdminRegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = Account
		fields = (
		'id', 'email', 'username', 'date_created', 'date_modified',
		'firstname', 'lastname', 'password', 'confirm_password', 'token' )
		read_only_fields = ('date_created', 'date_modified')


	def create(self, validated_data):
		return Account.objects.create_superuser(**validated_data)

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ('branch', 'year' ,'image')
