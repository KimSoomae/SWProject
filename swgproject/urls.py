"""swgproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from account import views
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/logout/', views.logout, name='logout'),
    path('home/',views.home,name="home"),
    #path('budget/',include ('budget.urls')),
    path('',views.home, name="home"),
    path('budget',views.budget,name="budget"),
    #path('budget_master',views.budget_master,name="budget_master"),
    path('budget/<groupname_budget>/budget_master',views.budget_master,name="budget_master"),
    path('budget/<groupname_budget>',views.confirm_budget,name="confirm_budget"),
    #path('budget/<groupname_budget>',views.reject_budget,name="reject_budget"),
    path('budget_usercheck',views.budget_usercheck,name="budget_usercheck"),

    

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)