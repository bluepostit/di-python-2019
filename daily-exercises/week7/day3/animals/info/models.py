from django.db import models

class Animal(models.Model):
	legs = models.SmallIntegerField()
	weight = models.FloatField()
	height = models.FloatField()
	speed = models.FloatField()
	family = models.ForeignKey('Family', on_delete=models.CASCADE)

	def is_quadruped(self):
		'''Does this animal have 4 legs?'''
		return self.legs == 4

class Family(models.Model):
	name = models.CharField(max_length=200)
