"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs', blogs),
    path('about', about, name="about"),
    path('', index, name="index"),
    path('create', create, name ="create"),
    path('change_password', change_password),
    path('register', register, name="register"),
    path('login', login, name="login"),
    path('logout', logout),
    path('extends', extends, name="extends"),
    path('<slug:txt>/update',update),
    path('<slug:txt>/delete',delete),
    path('<slug:txt>/profile',profile),
    path('<slug:txt>/comment', comment),
    path('<slug:txt>',  look_blog),
    
]
