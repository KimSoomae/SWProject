from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
     #path('budget_user',views.budget_user, name="budget_user"),
     #path('budget_admin',views.budget_admin,name="budget_admin"),
    path('budget',views.budget,name="budget"),
    path('logout',views.logout,name="logout"),
]