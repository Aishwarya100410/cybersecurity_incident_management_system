"""
URL configuration for Hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from home import views

urlpatterns = [
    path("",views.main,name='main'),
    path("adminlogin",views.adminlogin,name='adminlogin'),
     path("admindashboard",views.admindashboard,name='admindashboard'),
    path("userlogin",views.userlogin,name='userlogin'),
    path("register",views.register,name='register'),
    path("home",views.home,name='home'),
    path("about",views.about,name='about'),
    path("report",views.report,name='report'),
    path("logout",views.logout,name='logout'),
    path("analysis",views.analysis,name='analysis'),
     path("incidentmanagement",views.incidentmanagement,name='incidentmanagement'),
     path("settings",views.settings,name='settings'),
       path("severityl",views.severityl,name='severityl'),
    path("track",views.track,name='track'),
    path("tips",views.tips,name='tips') 
    
]