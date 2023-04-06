from django.shortcuts import render,redirect
from django.contrib import messages,auth
from .forms import UserForm
from .models import User,UserProfile
# Create your views here.
def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in...')
        return redirect('home')
    elif request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone_number=form.cleaned_data['phone_number']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,phone_number=phone_number)
            user.role=User.CUSTOMER
            user.save()
            email_subject = "Please active your account"
            email_template ="accounts/emails/account_varification.html"
            

            
    return render(request,'accounts/RegiserUser.html')



def customerDashboard(request):
    return render(request,'accounts/customerDashboard.html')


def sellerDashboard(request):
    return render(request,'accounts/sellerDashboard.html')
