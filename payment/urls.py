from django.urls import include,path
from . import views

urlpatterns = [
    
     path("paypal/", views.paypal,name="paypal")

      
   
]

