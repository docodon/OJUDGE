# At the top of your urls.py file, add the following line:
from django.conf import settings
from django.conf.urls import patterns , include , url
from django.contrib import admin
from pset import views



urlpatterns=patterns(' ',
	url(r'^$',views.admin_portal,name='admin_portal'),
	url(r'^login/$',views.login_user,name='login'),		
	url(r'^add_prob/$',views.add_problems,name='add_problems'),
	url(r'^add_cases/$',views.add_cases,name='add_cases'),
	url(r'^logout/$',views.logout_view,name='logout'),
	url(r'^start_contest',views.start_contest,name='start_contest'),
)

