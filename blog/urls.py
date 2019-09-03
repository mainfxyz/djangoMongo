"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import view


urlpatterns = [
    path('admin/', view.admin),
    path('',view.index),
    path('shop',view.shop),
    path('login',view.login),
    path('register',view.register),
    path('reg',view.reg),
    path('say',view.say),
    path('saveS',view.saveS),
    path('delS',view.delS),
    path('adminUser',view.adminUser),
    path('saveU',view.saveU),
    path('delU',view.delU),
]
