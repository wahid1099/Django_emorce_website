from django.urls import path,include

from . import views

urlpatterns=[
   

    path("<slug>/", views.get_product,name="get_product")
    
    

]  

