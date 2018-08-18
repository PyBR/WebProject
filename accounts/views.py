from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print (user)
    
    return render(request, 'accounts/login.html',{})

def home(request):

    return render(request, 'accounts/home.html')