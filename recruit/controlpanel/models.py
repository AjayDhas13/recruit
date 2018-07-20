# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid
import datetime

EDUCATION_CHOICES = (('BE', 'BE'), ('B-Tech', 'B-Tech'), ('BCA', 'BCA'))
GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
STATUSES = ((0, 'submitted'), (1, 'viewed'), (2, 'accepted'), (3, 'rejected'))

# Create your models here.
class Applications(models.Model):
	"""docstring for Applications"""
	ref_id = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	mobile = models.IntegerField()
	date_of_birth = models.DateField(blank=True, null=True)
	gender = models.CharField(choices=GENDER_CHOICES, max_length = 10, blank=True, null=True)
	education = models.CharField(
			max_length=25,
			blank=True,
			choices=EDUCATION_CHOICES,
		)
	profile = models.CharField(max_length=250)
	created_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	status = models.IntegerField(choices=STATUSES, default=STATUSES[0][0])
	
	def __unicode__(self):
		return self.name

	def save(self, force_insert=False, force_update=False):
		if not self.pk:
			self.ref_id = str(uuid.uuid1())
		self.created_at = datetime.datetime.now()
		super(Applications, self).save(force_insert, force_update)