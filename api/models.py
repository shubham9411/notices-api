from django.db import models
from datetime import datetime

class Api(models.Model):
	NOTICE_CHOICES = (
		('Official', 'Official'),
		('Class', 'Class'),
		('All', 'All'))

	BRANCH_CHOICES = (
		('CSE', 'CSE'),
		('BCE', 'BCE'),
		('ME', 'ME'),
		('ECE', 'ECE'),
		('EE', 'EE'),
		('CE', 'CE'),
		('CHE', 'CHE'))

	notice_name = models.CharField(max_length=20, null=True)
	notice_desc = models.TextField()
	notice_author = models.CharField(max_length=20)
	notice_valid_till = models.DateTimeField(default=datetime.now, blank=True)
	notice_publish_date = models.DateTimeField(auto_now=True)
	year = models.CharField(max_length=5, null=True)
	branch = models.CharField(max_length=20, null=True, default='None', choices=BRANCH_CHOICES)
	choices = models.CharField(max_length=1, null=True, default='All', choices=NOTICE_CHOICES)


	def __str__(self):
		return '%s' %self.notice_name