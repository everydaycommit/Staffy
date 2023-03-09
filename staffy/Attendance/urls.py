from django.urls import path
from .views import MyActivities,NewActivity

urlpatterns = [
    path('NewActivity',NewActivity),
    path('MyActivities',MyActivities),
]
