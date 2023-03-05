"""StaffManagement URL Configuration

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
from EMS.views import home,new_request,my_requests,new_activity,my_activities

urlpatterns = [
    path('',home,name='landing_page'),
    path('NewActivity/',new_activity,name='new_activity'),
    path('MyActivities/',my_activities,name='my_activities'),
    path('NewRequest/',new_request,name='new_request'),
    path('MyRequests/',my_requests,name='my_requests'),
    path('register/',my_requests,name='register'),
    path('login/',my_requests,name='login'),
    path('logout/',my_requests,name='logout'),
    path('admin/', admin.site.urls),
]
