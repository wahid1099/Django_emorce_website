from django.shortcuts import render,redirect
from django.contrib import messages,auth
from .forms import UserForm
from .models import User,UserProfile
from .utils import detectUser,send_email,send_notification
from seller.forms import SellerForm
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
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
            send_email(request,user,email_subject,email_template)
            messages.success(request,'Your account has been registered successfully,Please check your mail for confirmation')
            return redirect('home')
        else:
            messages.error(request,'Invalid data input')
    else:
        form=UserForm()
    
    context = {
        'form': form,
    }
    return render(request,'accounts/RegiserUser.html',context)



def registerSeller(request):
    if request.user.is_authenticated:
        messages.waring(request,'You are already logged in')
        return redirect('home')
    elif request.method == 'POST':
        form=UserForm(request.POST)
        seller_form=SellerForm(request.POST,request.FILES)
        if form.is_valid() and seller_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone_number=form.cleaned_data['phone_number']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,phone_number=phone_number)
            user.role=User.SELLER
            user.save()
            seller=seller_form.save(commit=False)
            seller.user=user

            user_profile=UserProfile.objects.get(user=user)
            seller.user_profile=user_profile
            seller.save()
            email_subject = "Please active your account"
            email_template ="accounts/emails/account_varification.html"
            send_email(request,user,email_subject,email_template)
            messages.success(request,'Your account has been registered successfully,Please check your mail for confirmation')
            return redirect('home')
        else:
            messages.error(request,'Invalid data found')
    else:
        form=UserForm()
        seller_form=SellerForm()
    
    context={
        'form': form,
        'seller_form':seller_form
    }
    return render(request,'accounts/Registerseller.html',context)



def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=User._default_manager.get(pk=uid)
    except (TypeError,ValueError,User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect('login')



def login(request):
    if request.user.is_authenticated:

        messages.warning(request,'You are already logged in')
    elif request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'sucessfully logged in!!!')
            return redirect('myaccounts')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login')
        return redirect(request,'accounts/login.html')
        
    

         


def logout(request):
    auth.logout(request)
    messages.info(request,'You are logged out!!!')
    return render(request,'accounts/login.html')


@login_required(login_url=login)
def myaccounts(request):
    user=request.user
    redirectUrl=detectUser(user)
    return redirect(redirectUrl)
            
    



def customerDashboard(request):
    return render(request,'accounts/customerDashboard.html')


def sellerDashboard(request):
    return render(request,'accounts/sellerDashboard.html')
