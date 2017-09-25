from django.db import models
from datetime import datetime

class Api(models.Model):
	notice_name = models.CharField(max_length=20, null=True)
	notice_desc = models.TextField()
	notice_author = models.CharField(max_length=20)
	notice_valid_till = models.DateTimeField(default=datetime.now, blank=True)
	notice_publish_date = models.DateTimeField(auto_now=True)


def __str__(self):
	return '%s' %self.notice_name