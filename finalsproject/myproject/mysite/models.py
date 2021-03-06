from __future__ import unicode_literals
from django.db import models

class Tips(models.Model):
	title=models.CharField(max_length=300,blank=False,unique=True)
	desc=models.TextField(blank=False)
	date_added = models.DateField(auto_now=False,auto_now_add=True)
	author=models.CharField(max_length=300,blank=False)
	imgdesc=models.FileField(null=True,blank=True)
	likes=models.IntegerField( default=0)
	dislikes=models.IntegerField( default=0)

	def __str__(self):
		return self.title
	class Meta:
		verbose_name="Tips"
