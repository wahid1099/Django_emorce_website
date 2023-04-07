from django.urls import include,path
from . import views

urlpatterns = [
     path("registerUser/", views.registerUser,name="registerUser"),
     path("customerDashboard/", views.customerDashboard,name="customerDashboard"),
     path("sellerDashboard/", views.sellerDashboard,name="sellerDashboard"),
     path("login/", views.login,name="login"),
     path("registerseller/", views.registerSeller,name="registerSeller"),
     path("logout/", views.logout,name="logout"),
     path("myaccount/", views.myaccounts,name="myaccounts"),
     path("activate/<uidb64>/<token>/", views.activate,name="activate"),
     path("forgot_password/", views.forgot_password,name="forgot_password"),
     path("reset_password_validate/<uidb64>/<token>/", views.reset_password_validation,name="reset_password_validate"),
     path("reset_password/", views.reset_password,name="reset_password"),

      
   
]

