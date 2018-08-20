#from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  url(r'^account/', include('accounts.urls')),
  path('', views.home, name='home'),
  path('polls/', include('polls.urls', namespace='polls'))

  
]




