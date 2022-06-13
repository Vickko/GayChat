"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from login import views

urlpatterns = [
    path('api/develop/signup/', views.Signup.as_view()),
    path('api/develop/login/', views.Login.as_view()),
    path('api/develop/Userprofile/', views.Userprofile.as_view()),
    path(r'group_found', views.group_found.as_view()),
    path(r'add_friend', views.add_friend.as_view()),
    path(r'delete_friend', views.delete_friend.as_view()),
    path(r'join_group', views.join_group.as_view()),
    path(r'retreat_group', views.retreat_group.as_view()),
]
