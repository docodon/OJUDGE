from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from forms import problems,testcases
from django.contrib.auth.decorators import user_passes_test,login_required
from datetime import datetime

# Create your views here.

def admin_portal(request):                   #first page for login....
	return render(request,'pset/admin_portal.html',{})


def login_user(request) :
	if request.user.is_authenticated():
		return render(request,'pset/admin_portal.html',{})
	
	if request.method=='POST':		
		user=authenticate(username=request.POST['name'],password=request.POST['password'])
		if user is not None:
			if user.is_active and user.is_superuser and user.is_staff :
				login(request,user)
				return render(request,'pset/admin_portal.html',{'success':request.POST['name']+'logged in succesfully'})
		else :
			return render(request,'pset/login.html',{'error':1})		
	return render(request,'pset/login.html',{})


@user_passes_test(lambda u: u.is_superuser,login_url='/setup/login')
def add_problems(request):
	if request.method=='POST':
		form=problems(request.POST)
		if form.is_valid() :
			form.save() 
			return render(request,'pset/admin_portal.html',{'success':request.POST['pcode']+'added succesfully'})
		else:
			return render(request,'pset/add_problems.html',{'form':problems(),'errors':'problem not validated'})	
	else:
		return render(request,'pset/add_problems.html',{'form':problems()})


@user_passes_test(lambda u: u.is_superuser,login_url='/setup/login')
def add_cases(request) :
	if request.method=='POST':
		form=testcases(request.POST,request.FILES)

		if form.is_valid() :
			form.save()
			return render(request,'pset/admin_portal.html',{'success':'test cases added for problem : '+request.POST['pcode']})
		else:
			return render(request,'pset/add_cases.html',{'form':testcases(),'error':1})
	else :
		return render(request,'pset/add_cases.html',{'form':testcases()})



@user_passes_test(lambda u: u.is_superuser,login_url='/setup/login')
def start_contest(request) :
	if request.method=='POST':
		st=str(request.POST['sdate']) + ' - ' + str(request.POST['stime'])   #string with start_time...
		et=str(request.POST['edate']) + ' - ' + str(request.POST['etime'])   #string with end_time
		stime=datetime.strptime(st,'%Y-%m-%d - %H:%M')
		etime=datetime.strptime(et,'%Y-%m-%d - %H:%M')
		if stime>etime :
			return render(request,'pset/start_contest.html',{'errors':'start time is greater than end time !!! '})
		
		request.session['cnt_stime']=stime;
		request.session['cnt_etime']=etime;
		
		return render(request,'pset/admin_portal.html',{'success':'contest time set  : '+str(stime)+' to '+str(etime) } )
	else :
		return render(request,'pset/start_contest.html',{})



@user_passes_test(lambda u: u.is_superuser,login_url='/setup/login')
def logout_view(request) :
    logout(request)
    return render(request,'pset/admin_portal.html',{'success':'logged out succesfully !!!'})
    # Redirect to a success page

