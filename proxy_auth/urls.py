"""proxy_auth URL Configuration

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
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView # new
from django.contrib.auth.decorators import login_required


import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(name)s %(levelname)s %(message)s',
)

def validate(request):
    if request.user.is_authenticated:
        return HttpResponse("yo", status=200)
    return HttpResponse("yo", status=401)

def home(request):
    return HttpResponse("home")

def login(request):
    logger = logging.getLogger("login")
    logger.info('login')
    return HttpResponse("login")


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', login),
    path('validate/', validate),
    path('admin/', admin.site.urls),
    path('dashboard/', include('django.contrib.auth.urls'))
]
