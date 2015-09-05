from django.conf import settings
from django.conf.urls import patterns , include , url
from django.contrib import admin
from contest import views

urlpatterns=patterns(' ',
	url(r'^$',views.contest_live,name='contest_live'),
	url(r'^login_team/$',views.login_team,name='login_team'),
	url(r'^problem/(?P<pname>.*)/$',views.probstate,name='problems'),
)



