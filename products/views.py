from django.shortcuts import render
from .models import * 
from tkinter import E
from django.contrib.auth.decorators import login_required
from accounts.views import *
from django.contrib import messages
from django.urls import reverse
from uuid import UUID
from products.models import *

@login_required(login_url=login)
def get_product(request , slug):
    try:
        product = Product.objects.get(slug=slug)
        # reviews = product.reviews.all()

        # reviews=Review.objects.filter(product=product.uid)
        reviews = Review.objects.filter(product__uid=product.uid)
        review_count = reviews.count()


        context = {
            'product' : product,
            'reviews':reviews,
            'review_count':review_count}
       
        return render(request  , 'product/product.html' ,context)

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



def review(request,product_id):
    #  url = reverse('review', kwargs={'product_id': str(product_id)})
     context = {"product_id": product_id}
     
     return render(request,'product/Review.html',context)


def addReview(request,product_id):
    print("prduct id from addReview",product_id)
    context = {"product_id": product_id}
    if request.method == 'POST':
        rating=request.POST.get('stars')
        author_name=request.POST.get('author_name')
        review_body=request.POST.get('review_body')
        author=request.user
        product=Product.objects.get(uid=product_id)
        messages.success(request,'Your review added succesfully!!')
        review=Review.objects.create(author_name=author_name,rating=rating,review_body=review_body,author=author,product=product)
        review.save()
        print(author_name,review_body,author,product)
        return render(request,'product/Review.html',context)
    return render(request,'product/Review.html')
    





def allproducts(reqest):
    products = Product.objects.all()
    context={
        'products':products,

    }

    return render(reqest, 'product/Allproducts.html',context)