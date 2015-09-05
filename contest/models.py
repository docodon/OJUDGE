from django.db import models

# Create your models here.

class teamr(models.Model):
	tname=models.CharField(max_length=10,unique=True)
	acs=models.IntegerField(default=0)
	time=models.DateTimeField()

	def __str__(self):
		return self.tname