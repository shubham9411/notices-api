from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.http import Http404

from .serializers import AccountSerializer, LoginSerializer
from .models import Account

class AuthRegister(APIView):
	"""
	Register a new user.
	"""
	serializer_class = AccountSerializer
	permission_classes = (AllowAny,)

	def get(self, request, format=None):
		allquery = Account.objects.all()
		serializer = AccountSerializer(allquery, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,
					status=status.HTTP_201_CREATED)
		return Response(serializer.errors,
		status=status.HTTP_400_BAD_REQUEST)

class AuthLogin(APIView):
    ''' Manual implementation of login method '''

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
	    data = request.data
	    serializer = LoginSerializer(data=data)
	    if serializer.is_valid(raise_exception=True):
	        new_data = serializer.data
	        return Response(new_data)
	    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)