#from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Usuário errado ou senha')
            #return HttpResponseRedirect(reverse('homepage'))
   
    return render(request, 'accounts/login.html')