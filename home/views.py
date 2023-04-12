from django.shortcuts import render
from products.models import * 
from tkinter import E
from django.contrib.auth.decorators import login_required
from accounts.views import *
from django.contrib import messages


# Create your views here.


def Contactus(request):
    return render(request,'home/Contactus.html')


def home(request):
    all_categories =Category.objects.all()
    products = Product.objects.all()
    context = {
        'category':all_categories,
        'products':products
    }
    return render(request,'index.html',context)



