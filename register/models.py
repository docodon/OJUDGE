from django.db import models

# Create your models here.

class team(models.Model) :
	name=models.CharField(max_length=50,unique=True) ;
	member1=models.CharField(max_length=100) ;
	member2=models.CharField(max_length=100) ;
	member3=models.CharField(max_length=100) ;
	password=models.CharField(max_length=100);	
	
	def __str__(self) :
		return self.name;

