from rest_framework import serializers
from .models import Api

class ApiSerializers(serializers.ModelSerializer):
	class Meta:
		model = Api
		fields = ('id', 'task_name', 'task_desc', 'task_created')