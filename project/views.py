#from django.http import HttpResponseRedirect
#from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages


# Create your views here.


def home(request):
    context = {}
    return render(request, 'home.html', context)
    
def accounts(request):
    return render(request, 'accounts/login.html')


   
    
    