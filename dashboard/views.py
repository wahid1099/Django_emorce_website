from django.shortcuts import render,redirect
from products.models import *
from django.contrib import messages
from products.models import *
from order.models import *
from accounts.models import *
import os
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

def cutomerreviews(request):
    user=request.user
    userreivew=Review.objects.filter(author_id=user)
    # Product=Product.objects.get()
    

     
    context={
        'allreview':userreivew,
        

    }
    return render(request, 'accounts/CustomerReivews.html',context)


def userprofile(request):
    user=request.user
    try:
     userprofile=UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        messages.error(request, "Userprofile does not exist")

    print("user",user)
    print("user",userprofile)
    

    context={
        'user':user,
        'userprofile':userprofile
    }
    if request.method == 'POST' :
        if len(request.FILES) !=0:
 
           if 'profile_picture' in request.FILES:

             os.remove(userprofile.profile_picture.path)
             userprofile.profile_picture=request.FILES['profile_picture']
          

        userprofile.adress_line_1=request.POST.get('adress_line_1')
        userprofile.state=request.POST.get('state')
        userprofile.pin_code=request.POST.get('pin_code')
        userprofile.city=request.POST.get('city')
        user.phone_number=request.POST.get('phone_number')
       
        userprofile.save()
        user.save()
        messages.success(request,"Profile updated SuccessFully!!")
        return render(request, 'accounts/Profile.html',context)

    
    return render(request, 'accounts/Profile.html',context)