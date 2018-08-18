#from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  url(r'^account/', include('accounts.urls')),
]




