from django.contrib import admin
from .models import profile
# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display = ('user', 'studentnum','groupname','major','name')
admin.site.register(profile, userAdmin)


