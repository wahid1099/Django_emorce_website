

from django.urls import include,path
from . import views

urlpatterns = [
   
    path('dashbordhome/',views.dashboard,name='dashbordhome'),
   
]

