from django.shortcuts import render, HttpResponse

#Create views here.
def home(request):
    return render(request, 'accounts/login.html')