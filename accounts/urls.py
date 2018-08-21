from django.urls import path
from . import views
from django.contrib.auth import login


app_name="accounts"
urlpatterns = [
    path('login/', views.login_user, name="login"),

    

    
]