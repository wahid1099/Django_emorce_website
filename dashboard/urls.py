

from django.urls import include,path
from . import views

urlpatterns = [
   
    path('dashboardHome/',views.dashboardHome,name='dashboardHome'),
    path('CustomerOrders/',views.CustomerOrders,name='CustomerOrders'),
   
]

