from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from . import views

# Create your views here.

def budget_user(request):
    return render(request,'budget_user.html')
def budget_admin(request):
    return render(request,'budget_admin.html')