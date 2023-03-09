"""staffy URL Configuration

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
from django.urls import path, include
from django.contrib.auth import login,logout
from Core.views import home, register
from Attendance import urls as att_urls
from LeaveRequest import urls as LR_urls
from ProductRequest import urls as PR_urls
from ReadingBoard import urls as RB_urls
from Retro import urls as Retro_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='landing_page'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('attendance/',include(att_urls)),
    path('leaveRequest/',include(LR_urls)),
    path('productRequest/',include(PR_urls)),
    path('readingBoard/',include(RB_urls)),
    path('retro',include(Retro_urls))
]
