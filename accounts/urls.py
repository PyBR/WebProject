from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import login
from django.views.generic.base import TemplateView

from django.contrib import admin

app_ame="accounts"
urlpatterns = [
    path('login/', views.login_user, name="login"),
    url(r'^$', views.home),
    url(r'^login/$', TemplateView.as_view(template_name="accounts/login.html")),
    

    
]