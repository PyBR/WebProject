from django.shortcuts import render


#Create views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)
    
def accounts(request):
    return render(request, 'accounts/login.html')
   
    
    