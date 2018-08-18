from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
import datetime

#Create views here.

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    now = datetime.datetime.now()
    context = {'datetime_now':now}
    return render(request, 'home.html', context)
    
def accounts(request):
    return render(request, 'accounts/login.html')
   
    
    