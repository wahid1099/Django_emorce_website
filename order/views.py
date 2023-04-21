from django.shortcuts import render,redirect
from products.models import *
from accounts.models import *
from .models import *
from accounts.utils import *
from django.forms.models import model_to_dict
from django.contrib import messages,auth


# Create your views here.


def checkout_product(request, slug):
   
      product = Product.objects.get(slug=slug)
    
      return render(request, 'product/Checkout.html', {'product': product})




def place_order(request,slug):
       if request.method=="POST":
        product=Product.objects.get(slug=slug)
        phone_no=request.POST.get('phone')
        adress=request.POST.get('adress')
        name=request.POST.get('fullName')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zipcode=request.POST.get('zipcode')
        payment_method=request.POST.get('payment')
        price=product.price
        user=request.user
        userprofile=User.objects.get(email=user.email)
        print("Payment method",payment_method)
        if payment_method=='cash':
             order=Order(
                  
                  user=user,
                  product=product,
                  price=price,
                  phone_no=phone_no,
                  adress=adress,
                  city=city,
                  state=state,
                  zipcode=zipcode,
                  payment_Type=payment_method
                 


             )
             order.save()
             order_confirmation_mail(request,userprofile)
             messages.success(request, "Order Placed Sucessfully")
             return render(request,'product/Orderplaced.html')
        elif payment_method=='paypal':
              return render(request,'payment/paypal.html')
        
        return redirect('home')



def order_confirmation_mail(request, userprofile):
      email_subject="Order Placed Sucessfully!"
      email_template="accounts/emails/OrderPlacedMail.html"
      context={
           'user':userprofile
      }
     
      send_notification(email_subject,email_template,context)
