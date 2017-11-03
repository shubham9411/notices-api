from django.conf.urls import url
from .views import AddNotice

urlpatterns = [
	url(r'^addnotices/$', AddNotice.as_view()),
]
