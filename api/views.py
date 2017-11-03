from django.shortcuts import render
from .models import Api
from rest_framework import viewsets
from rest_framework.views import APIView
from .Serializers import ApiSerializer, AddNoticeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response

class ApiViewSet(viewsets.ModelViewSet):

	permission_class = (AllowAny,)
	serializer_class = ApiSerializer
	queryset = Api.objects.all().order_by('-notice_publish_date')

class AddNotice(APIView):

	permission_class = (IsAuthenticated,)
	serializer_class = AddNoticeSerializer
	def post(self, request, format=None):
		data = request.data
		serializer = AddNoticeSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			new_data = serializer.data
			return Response(new_data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
