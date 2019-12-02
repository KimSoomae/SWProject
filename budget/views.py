from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from . import views
from .models import Budget_list

# Create your views here.

#def budget_user(request):
#    return render(request,'budget_user.html')

#def budget_admin(request):
#    return render(request,'budget_admin.html')

#def budget(request):
#    if request.user.is_superuser:
#        return render(request,'budget_admin.html')
#    else:
#        return render(request,'budget_user.html')

def budget(request):
    if request.user.is_superuser:
            return render(request,'budget_admin.html')
    else:
        budget_user=Budget_list.objects.all()
        context={'budget_user': budget_user}
        try:
            budgetUser=Budget_list(num=request.POST['num'], item=request.POST['item'],quantity=request.POST['quantity'],price=request.POST['price'],qxp=request.POST['qxp'],check=request.POST['check'] )
            budgetUser.save()
        except:
            budgetUser=None
        return render(request,'budget_user.html',context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')