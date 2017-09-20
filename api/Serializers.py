from rest_framework import serializers
from .models import Api

class ApiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Api
		fields = ('id', 'notice_name', 'notice_desc', 'notice_author', 'notice_valid_till', 'notice_publish_date')