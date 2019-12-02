from django.contrib import admin
from .models import Budget_list
# Register your models here.

class budgetAdmin(admin.ModelAdmin):
    list_display = ('num', 'item', 'quantity', 'price', 'qxp', 'check')
admin.site.register(Budget_list, budgetAdmin)