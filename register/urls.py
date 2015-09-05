from django.conf.urls import patterns , include , url
from django.contrib import admin
from register import views

urlpatterns=patterns('',
	url(r'^$',views.home,name='home') ,
	url(r'^register/$',views.register,name='register'),
)