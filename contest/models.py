from django.db import models

# Create your models here.

class teamr(models.Model):
	tname=models.CharField(max_length=10,unique=True)
	acs=models.IntegerField(default=0)
	time=models.DateTimeField()

	class Meta :
		ordering = ['-acs', 'time']

	def __str__(self):
		return self.tname


class accepted(models.Model):
	pcode=models.CharField(max_length=10)
	tname=models.CharField(max_length=10)
	code=models.TextField()

	def __str(self):
		return self.tname