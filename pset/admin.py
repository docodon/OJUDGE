from django.contrib import admin
from pset.models import problem,testcases,timer

# Register your models here.
admin.site.register(problem) 
admin.site.register(testcases) 
admin.site.register(timer)