from django.shortcuts import render
from products.models import *
from django.contrib import messages
from order.models import *
# Create your views here.




def dashboardHome(request):
    return render(request, 'accounts/Dashboard.html')


def CustomerOrders(request):
    user=request.user
    userorder=Order.objects.filter(user=user)
    

     
    context={
        'allorder':userorder,
        

    }
    return render(request, 'accounts/CustomerOrder.html',context)