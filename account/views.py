from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib.auth import get_user_model,login, authenticate
from django import forms
from .forms import UserCreationMultiForm,UserCreationForm
from .models import profile


# Create your views here.
def signup(request):
    if request.method=="POST":
        form = UserCreationMultiForm(request.POST)
        if form.is_valid():
            User = form['user'].save()
            #print(form['signup'])
            new_user = form['signup'].save(commit=False) 
            new_user.user = User
            new_user.save()
            return redirect('login')
    else:
        form=UserCreationMultiForm()
    return render(request,'signup.html',{'form':form})


# def signup(request):
#     if request.method=='POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1'], groupname=request.POST['groupname'], studentnum=request.POST['studentnum'], major=request.POST['major'])
#             auth.login(request, user)
#             return redirect('home')
#     return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request,username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')

def home(request, teamList=None):
    try:
        TeamList = request.user.team_set.all().values()
    except:
        TeamList = None
    return render(request, 'home.html',{'Teams':TeamList})
