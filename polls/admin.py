from django.contrib import admin

from .models import Choice, Poll
from  .models import Poll
# Register your models here.
admin.site.register(Choice)
admin.site.register(Poll)