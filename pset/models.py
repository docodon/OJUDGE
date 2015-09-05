from django.db import models

# Create your models here.
class problem(models.Model) :
	pcode=models.CharField(max_length=10,unique=True)
	pdesc=models.TextField() 
	
	def __str__(self) :
		return self.pcode	

class testcases(models.Model):
	pcode=models.CharField(max_length=10)
	inp=models.FileField(upload_to='testcases',blank=True)
	out=models.FileField(upload_to='testcases',blank=True)

	def __str__(self):
		return self.pcode