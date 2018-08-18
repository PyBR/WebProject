#from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  url(r'^account/', include('accounts.urls')),
  path('time/', views.current_datetime),
  path('home/', views.home)
  
]




