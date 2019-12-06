from django.urls import path
from . import views
urlpatterns=[
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('',views.home, name="home"),
    path('budget',views.budget,name="budget"),
    path(r'^budget_master/(?P<groupname_budget>.+)', views.budget_master),
    #path('budget_master',views.budget_master,name="budget_master"),

]