from django.contrib import admin
from .models import profile
from .models import Budget_list
from . import views
# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display = ('user', 'studentnum','groupname','major','name')
admin.site.register(profile, userAdmin)

class budgetAdmin(admin.ModelAdmin):
    list_display = ('num', 'item', 'quantity', 'price', 'qxp', 'groupname_budget', 'people','state')
admin.site.register(Budget_list, budgetAdmin)
