from django.conf.urls import url
from .views import AuthRegister, AuthLogin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	url(r'^register/$', AuthRegister.as_view()),
	url(r'^login/$', AuthLogin.as_view()),
]