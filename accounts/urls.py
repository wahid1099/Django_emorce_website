from django.urls import include,path
from . import views

urlpatterns = [
     path("registerUser/", views.registerUser,name="registerUser"),
     path("customerDashboard/", views.customerDashboard,name="customerDashboard"),
      path("sellerDashboard/", views.sellerDashboard,name="sellerDashboard")
   
]

