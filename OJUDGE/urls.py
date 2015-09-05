from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns=patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^home/',include('register.urls')),
    url(r'^setup/',include('pset.urls')),
    url(r'^contest/',include('contest.urls')),
)



# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), 
)