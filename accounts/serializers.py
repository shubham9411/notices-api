from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Account
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist

class AccountSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True)
	confirm_password = serializers.CharField(write_only=True,
	required=True)

	# token = serializers.CharField(max_length=255, read_only=True)

	class Meta:
		model = Account
		fields = (
		'id', 'email', 'username', 'date_created', 'date_modified',
		'firstname', 'lastname', 'password', 'confirm_password')
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

	def validate(self, data):
		'''
		Ensure the passwords are the same
		'''
		if data['password']:
			if data['password'] != data['confirm_password']:
				raise serializers.ValidationError(
					"The passwords have to be the same"
		)
		return data

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid". In the case of logging a
        # user in, this means validating that they've provided an email
        # and password and that this combination matches one of the users in
        # our database.
        email = data.get('email', None)
        password = data.get('password', None)

        # Raise an exception if an
        # email is not provided.
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        # Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `email` as the `username` value since in our User
        # model we set `USERNAME_FIELD` as `email`.
        user = authenticate(username=email, password=password)

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
