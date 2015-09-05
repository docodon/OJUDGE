from django.db import models
from django import forms
from register.models import team

class team(forms.ModelForm) :
	class Meta:
		model=team
		fields=['name','member1','member2','member3','password']
		widgets={
			'password':forms.PasswordInput(),
		}

		