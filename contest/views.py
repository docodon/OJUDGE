from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from pset.models import problem , testcases 
from contest.models import teamr
# Create your views here.

def login_team(request) :
	if request.method=='POST':
		
	else :
		return render(request,'contest/login_team.html',{})

def contest_live(request) :
	tup=(x for x in problem.objects.values_list('pcode',flat=True))
	return render(request,'contest/contest_live.html',{'list':tup})

def probstate(request,pname) :
	print pname

