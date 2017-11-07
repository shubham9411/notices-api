from rest_framework import serializers
from .models import Api

class ApiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Api
		fields = ('id', 'notice_name', 'notice_desc', 'notice_author', 'notice_valid_till', 'notice_publish_date','year', 'branch', 'choices')

class AddNoticeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Api
		fields = ('id', 'notice_name', 'notice_desc', 'notice_author', 'notice_valid_till', 'notice_publish_date','year', 'branch', 'choices')

	def create(self, validated_data):
			return Api.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.notice_name =  validated_data.get('name', instance.notice_name)
		instance.notice_desc = validated_data.get('category', instance.notice_desc)
		instance.notice_author = validated_data.get('subcategory', instance.notice_author)
		instance.notice_valid_till = validated_data.get('subcategory', instance.notice_valid_till)
		instance.notice_publish_date = validated_data.get('subcategory', instance.notice_publish_date)
		instance.choices = validated_data.get('choices', instance.choices)
		instance.save()
		return instance

class Notice_Year_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Api
		fields = ('year',)

class Notice_Branch_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Api
		fields = ('branch',)

class Notice_Branch_Year_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Api
		fields = ('branch', 'year')

