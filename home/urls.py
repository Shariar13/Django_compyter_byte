from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
   
    path('',views.home,name='home'),
    path('front_end',views.front_end.as_view(),name='front_end'),
    path('back_end',views.back_end.as_view(),name='back_end'),
    path('fullstack',views.fullstack.as_view(),name='fullstack'),
    path('front_end_form',views.front_end_form,name='front_end_form'),
    path('back_end_form',views.back_end_form,name='back_end_form'),
    path('fullstack_form',views.fullstack_form,name='fullstack_form'),
    path('signinn',views.signinn,name="signinn"),
    path('signup/',views.signup,name="signup"),
    path('signout/',views.signout,name="signout"),
    path('browse_project/',views.browse_project.as_view(),name="browse_project"),

    


    
    
  
]