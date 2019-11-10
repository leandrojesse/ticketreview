from django.contrib import admin
from .models import Host
from .models import Tickethost

# Register your models here.
admin.site.register(Host)
admin.site.register(Tickethost)