from django.shortcuts import render
from .models import Api
from rest_framework import viewsets
from .Serializers import ApiSerializer

class ApiViewSet(viewsets.ModelViewSet):
	queryset = Api.objects.all()
	serializer_class = ApiSerializer
