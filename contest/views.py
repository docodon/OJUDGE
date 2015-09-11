from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from pset.models import problem , testcases 
from contest.models import teamr,accepted
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import logout 
from pset.models import timer
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

#ideone-----------------------------------------------------------------------------------------

import suds
from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import
from time import sleep

#ideone-----------------------------------------------------------------------------------------


# Create your views here.

def login_team(request) :
	if request.method=='POST':
		usr=authenticate(username=request.POST['name'],password=request.POST['password'])
		if usr is not None :
			login(request,usr)
			try :
				usr=teamr.objects.get(tname=request.POST['name']) 
			except:
				teamin=teamr(tname=request.POST['name'],acs=0,time=datetime.datetime.now())
				teamin.save()
							
			return redirect('contest_live')	
		else :
			return render(request,'contest/login_team.html',{'errors':'Team not recognized kindly fill your details again !!!'})
	
	else :
		return render(request,'contest/login_team.html',{})



@login_required(login_url='/contest/login_team')
def contest_live(request):
	tup=tuple()
	ttl=int(0)
	
	tup=(x for x in problem.objects.values_list('pcode',flat=True))
	
	ti_me=ch_time(1)
	
	if ti_me==None :
		return render(request,'contest/contest_live.html',{'time_message':'No contest yet scheduled !!!'})

	print ti_me
	crnt_time=timezone.localtime(timezone.now())
		
	if ti_me['st']>crnt_time :
		return render(request,'contest/contest_live.html',{'time_message':'Contest not yet started !!!'})

	if ti_me['et']<crnt_time :
		return render(request,'contest/contest_live.html',{'time_message':'Contest is over !!!'})
				
	tleft=ti_me['et'] - timezone.localtime(timezone.now())
	ttl=int(tleft.days*86400 + tleft.seconds)
	print ti_me['et'] ,'   ',datetime.datetime.now()
		
	return render(request,'contest/contest_live.html',{'list':tup,'time_left':ttl})



#THIS IS WHERE THE PROGRAM IS GOING TO BE COMPILED BY IDEONE AND CHECKED.....................

#@user_passes_test(ch_time(),login_url='/contest/login_team')
@login_required(login_url='/contest/login_team')
def probstate(request,pname) :
	if not ch_time() :
		print '00000000000000000000000000000000000000000000000000000000000000'
		return redirect('contest_live')


	url='https://ideone.com/api/1/service.wsdl'
	user='docodon'
	key='ju#4567'
	imp = Import('http://schemas.xmlsoap.org/soap/encoding/')  #simply cut-paste but i think it solves the namespace sort of issues   
	imp.filter.add('http://ideone.com/api/1/service')          #https://fedorahosted.org/suds/ticket/220  (last comment)
	d = ImportDoctor(imp)                                      #without this was not able to fetch from api
	
	if request.method=='POST' :
		source_code=request.POST['code']
		tests=testcases.objects.filter(pcode=pname)   #
		l_id=request.POST.get('lang')
		
		RESULT='Accepted'

		for cs in tests :
			stdin=cs.inp.read()
			output=cs.out.read()
			sud_client=Client(url,doctor=d)

			sub=sud_client.service.createSubmission(user,key,source_code,l_id,stdin,True, True)
			link=sub['item'][1]['value'][0]                   #somehow pinned out the link...
        	
			stts=sud_client.service.getSubmissionStatus(user,key,link)    #checking status if status==0 program executed 
        
			while stts['item'][1]['value'][0]!=0:          
				sleep(2)	
				stts=sud_client.service.getSubmissionStatus(user,key,link)

			result=sud_client.service.getSubmissionDetails(user,key,link,True,True,True,True,True)
		
			gen=dict()
		
			for i in result[0] :                               # mostly i made hit & trial for picking up values ...
				gen[i[0][0]]=i[1][0]
			
			res=gen['result']

			print output,' -------- ',gen['output']
			clr='#000000'

			if res==11 :
				RESULT='Compilation error '+gen['cmpinfo']
				clr='yellow'
				break
			elif res==15 and gen['output'] != output :
				RESULT='Wrong answer'
				clr='red'
				break
			elif res==12:
				RESULT='Runtime error'
				clr='red'
				break
			elif res==13:
				RESULT='Time limit exceeded'
				clr='yellow'
				break
			elif res==17:
				RESULT='Memory limit exceeded'
				clr='red'
				break

		print RESULT
		print request.user

		if RESULT=='Accepted' :
			try:
				clr='green'
				o=accepted.objects.get(pcode=str(pname),tname=str(request.user)) 
			except:
				obj=accepted(pcode=pname,tname=request.user,code=source_code)
				obj.save()
				obj2=teamr.objects.get(tname=request.user)
				obj2.acs=obj2.acs+1
				obj2.time=datetime.datetime.now()
				obj2.save()

		return render(request,'contest/result.html',{'success':RESULT,'color':clr})

	else :	
		sud_client = Client(url,doctor=d)
		lang_list =sud_client.service.getLanguages(user,key)      #method called using suds_client.service.method  
		
		lang_list=list(list(lang_list)[0][1][1][1])    #and store it in a list of dictionaries named lang
		languages=list()

		for i in lang_list[0][0] :
			temp=dict()
			temp['key']=i[0][0]
			temp['value']=i[1][0]
			languages.append(temp)
		pst=problem.objects.get(pcode=pname)
		return render(request,'contest/problem_statement.html',{'problem':pst,'lang':languages})	

#@user_passes_test(ch_time(),login_url='/contest/login_team')
@login_required(login_url='/contest/login_team')
def logout_view(request):
	logout(request)
	return render(request,'contest/login_team.html',{})

#@user_passes_test(ch_time(),login_url='/contest/login_team')
@login_required(login_url='/contest/login_team')
def rankings(request):
	if not ch_time() :
		return redirect('contest_live') 
	tup1=teamr.objects.all()
	tup=dict()
	
	for i in range(0,len(tup1)) :
		tup[i+1]=tup1[i]
	print tup	
	return render(request,'contest/rankings.html',{'list':tup,'ran':0})



def ch_time(arg=None) :
	tim=timezone.localtime(timezone.now())

	try :
		inter=timer.objects.all()
	except: 
		return redirect('contest_live') 

	if len(inter)==0:
		if arg==1 :
				return None
		return False  


	st=inter[0].stime 
	et=inter[0].etime 
	
	if arg==1 :
		return {'et':et,'st':st}
	
	if st > tim :
		return False  #redirect('contest_live')  #HttpResponseRedirect(reverse('contest_live', kwargs={'time_message':'Contest not yet started !!!' })) #redirect('contest_live',time_message='Contest not yet started !!!')
	if 	et < tim :
		return False  #redirect('contest_live')  #HttpResponseRedirect(reverse('contest_live', kwargs={'time_message':'Contest over !!!' })) #redirect('contest_live',time_message='Contest over !!!')
 	else :
 		return True
