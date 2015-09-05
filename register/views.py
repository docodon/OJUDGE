from django.shortcuts import render
from django.contrib.auth.hashers import PBKDF2PasswordHasher,make_password
from register.forms import team
# Create your views here.

def home(request) :
	return render(request,'home.html',{}) ;


def register(request) :
	error=''
	if request.method=='POST' :
		form=team(request.POST) 

		if form.is_valid() :
			use=form.save(commit=False)
			use.password=make_password(form.cleaned_data['password'])
			use.save()
			return render(request,'home.html',{'success':1}) ;
		else :	
			error=form.errors
	
	return render(request,'register.html',{'form':team(),'error':error}) ;