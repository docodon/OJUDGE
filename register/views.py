from django.shortcuts import render
from django.contrib.auth.hashers import PBKDF2PasswordHasher,make_password,check_password
from register.forms import team
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import logout 


# Create your views here.

def home(request) :
	return render(request,'home.html',{}) ;


def register(request) :
	error=''
	
	if request.method=='POST' :
		form=team(request.POST)  				
		if form.is_valid() :   				  	
			use=form.save(commit=False)         
			u=User.objects.create_user(form.cleaned_data['name']) #user object made using name....	
			u.set_password(form.cleaned_data['password'])
			u.save()
			use.password=make_password(form.cleaned_data['password'])
			use.user=u
			use.save()
			return render(request,'home.html',{'success':use.name+' team registered succesfully !!!!'}) ;
		else :	
			error=form.errors
			return render(request,'register.html',{'form':team(),'error':'something wrong please check !!'}) ;		
	return render(request,'register.html',{'form':team(),'error':error}) ;


def logout_reg(request):
	usr=request.user
	logout(request)
	return render(request,'home.html',{'success':str(usr) + '  succesfully loggged out !!!'})