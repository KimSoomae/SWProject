from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model,login, authenticate
from django import forms
from .forms import UserCreationMultiForm,UserCreationForm
from .models import profile
from . import views
from .models import Budget_list
from django.views.decorators.csrf import csrf_exempt


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

def home(request):
    return render(request, 'index.html')

def budget(request):
    if request.user.is_superuser:
        budget_user=Budget_list.objects.all()
        for i in range(len(budget_user)):
            priceTempList = budget_user[i].price.split('-')
            quantityTempList = budget_user[i].quantity.split('-')
            budget_user[i].total_price = 0
            
            print(priceTempList, quantityTempList)
            for j in range(len(priceTempList)):
                if(priceTempList[j] != '' and quantityTempList[j] != ''):
                    budget_user[i].total_price += int(priceTempList[j]) * int(quantityTempList[j])
            
        context={'budget_user': budget_user}
        return render(request,'budget_admin.html',context)
    else:
        if request.method == 'POST':
            print('All',request.POST)
            allPrice = request.POST.getlist('price')
            allQuantity = request.POST.getlist('quantity')
            # allQXP = []
            # for i in range(len(allPrice)):
            #     temp = int(allPrice[i]) * int(allQuantity[i])
            #     numberedString = str(temp)
            #     allQXP.append(numberedString)
            # print(allQXP)


            quantityString = '-'.join(request.POST.getlist('quantity'))
            itemString = '-'.join(request.POST.getlist('item'))
            priceString = '-'.join(request.POST.getlist('price'))
            

            print(quantityString, itemString, priceString)

            budget_user=Budget_list.objects.all()
            context={'budget_user': budget_user}
            try:
                print('saved?')
                budgetusers=Budget_list(num='', item=itemString, quantity=quantityString ,price=priceString, qxp='', total='' ,groupname_budget=request.POST['groupname_budget'], people=request.POST['people'] )
                budgetusers.save()
                print('saved')
            except:
                print('not saved')
                budgetusers=None
                print('not saved')
            return render(request,'budget_user.html',context)
        return render(request,'budget_user.html')

def budget_master(request,groupname_budget):
    budget_user=Budget_list.objects.filter(groupname_budget=groupname_budget)
    context={'budget_user': budget_user, 'groupname_budget':groupname_budget }
    print(budget_user[0].state)
    item = budget_user[0].item.split('-')
    quantity = budget_user[0].quantity.split('-')
    price = budget_user[0].price.split('-')
    result = []
    print(item)
    total = 0
    for index in range(len(item)):
        if len(item[index]) == 0:
            break
        qxp = int(price[index]) * int(quantity[index])
        print(qxp)
        total += qxp
        temp = {
            'item' : item[index],
            'price' : price[index],
            'quantity' : quantity[index],
            'qxp' : qxp,
        }
        result.append(temp)
       
    
    context = {
        'result' : result,
        'groupname_budget':groupname_budget,
        'total' : total      
    }
    return render(request,'budget_master_check.html',context)

def confirm_budget(request,groupname_budget):
    budget_user=Budget_list.objects.get(groupname_budget=groupname_budget)
    if request.method == "POST" :
        # print(request.POST["confirm"])
        try: 
            request.POST["confirm"] == "confirm"
            try:
                # budget_user.update(state= 1 )
                budget_user.state = 1

                print('승인버튼누름')
                #budget_user[0].state = 1 
                print(budget_user.state)
                budget_user.save()
                #for object in budget_user:
                #    object.save()
                
            except:
                pass
        except:
            try:
                # budget_user.update(state= 1 )
                budget_user.state = 2

                print('반려버튼누름')
                #budget_user[0].state = 1 
                print(budget_user.state)
                budget_user.save()
                #for object in budget_user:
                #    object.save()
                
            except:
                pass

    context= {budget_user: budget_user}
    return render(request,'budget_admin.html',context)

def budget_usercheck(request):
    if request.user.is_authenticated:
        budget_user=Budget_list.objects.all()
        for i in range(len(budget_user)):
                priceTempList = budget_user[i].price.split('-')
                quantityTempList = budget_user[i].quantity.split('-')
                budget_user[i].total_price = 0
                
                print(priceTempList, quantityTempList)
                for j in range(len(priceTempList)):
                    if(priceTempList[j] != '' and quantityTempList[j] != ''):
                        budget_user[i].total_price += int(priceTempList[j]) * int(quantityTempList[j])
            
        context={'budget_user': budget_user}
        return render(request,'budget_usercheck.html',context)