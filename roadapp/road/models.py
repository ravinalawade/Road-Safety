from django.db import models

class Blackspot(models.Model):
	lat = models.FloatField(max_length=20)
	log = models.FloatField(max_length=20)
	location = models.CharField(max_length=200,default='loc')
	def __str__(self):
		return self.location

class Sharpturn(models.Model):
	lat = models.FloatField(max_length=20)
	log = models.FloatField(max_length=20)
	location = models.CharField(max_length=200,default='loc')
	def __str__(self):
		return self.location

