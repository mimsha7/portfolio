from django.contrib import admin
from .models import Service,Portfolio,Team,About,Contact
# Register your models here.
admin.site.register([Service,Portfolio,Team,About,Contact])