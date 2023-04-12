from django.shortcuts import render
from .models import * 
from tkinter import E
from django.contrib.auth.decorators import login_required
from accounts.views import *


@login_required(login_url=login)
def get_product(request , slug):
    try:
        product = Product.objects.get(slug=slug)
        return render(request  , 'product/product.html' , context = {'product' : product})

    except Exception as e:
       
       messages.error(request, e)

        
    

# @login_required(login_url=login)
# def checkout_product(request,slug):
#     try:
#        product = Product.objects.get(slug=slug)
#        context = {'product' : product}
#        return render(request, 'product/Checkout.html',context)
#     except Exception as e:
#        messages.error(request, e)

def checkout_product(request, slug):
    # retrieve the product with the given slug from the database
    product = Product.objects.get(slug=slug)
    
    # do some processing
    
    # return an HTTP response
    return render(request, 'product/Checkout.html', {'product': product})
    