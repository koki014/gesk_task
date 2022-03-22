from django.contrib import admin
from .models import Payload
# Register your models here.

admin.site.site_header = "Gesk Task Admin"
admin.site.site_title = "Gesk Task Admin Portal"
admin.site.index_title = "Welcome to Gesk Task Admin Portal"

admin.site.register(Payload)

