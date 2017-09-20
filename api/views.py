from django.shortcuts import render
from .models import Api
from rest_framework import viewsets
from .Serializers import ApiSerializer

class ApiViewSet(viewsets.ModelViewSet):
	queryset = Api.objects.all().order_by('-notice_publish_date')
	serializer_class = ApiSerializer
