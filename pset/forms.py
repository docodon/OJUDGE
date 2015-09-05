from django.db import models
from django import forms
from pset.models import problem , testcases 
from django.contrib.admin import widgets

class problems(forms.ModelForm):
	class Meta:
		model=problem
		fields=['pcode','pdesc']

class testcases(forms.ModelForm):
	class Meta:
		model=testcases
		fields=['pcode','inp','out']

	def __init__(self,*args,**kwargs):
		super(testcases,self).__init__(*args,**kwargs)
		self.fields['pcode']=forms.ChoiceField(choices=get_list())



def get_list() :
	tup=((x,x) for x in problem.objects.values_list('pcode',flat=True))
	return tup