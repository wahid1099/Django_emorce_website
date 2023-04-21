from django.urls import include,path
from . import views

urlpatterns = [
    
     path("registerUser/", views.registerUser,name="registerUser"),

      
   
]

