from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Payment
# Create your views here.



def payment(request):
    # mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_KEY)
    pass
