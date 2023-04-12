from django.conf import settings
from django.contrib.sites.shortcuts import  get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator

from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
#   CUSTOMER=1
#     SELLER=2

def detectUser(user):
    if user.role == 1:
        return 'customerDashboard'
    elif user.role == 2:
        return 'sellerDashboard'
    elif user.role is None and user.is_superuser:
        return '/admin'


def send_email(request,user,email_subject,email_template):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site=get_current_site(request)
    message=render_to_string( email_template,{
        'user':user,
        'domain':current_site,
         'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':default_token_generator.make_token(user)

        } )
    to_email=user.email
    mail=EmailMessage(
        email_subject,
        message,
        from_email,
        to=[to_email])
    mail.send()


def send_notification(email_subject, email_template,context):
    from_email=settings.DEFAULT_FROM_EMAIL
    messages=render_to_string(
        email_template,context
    )
    to_email=context['user'].email
    mail=EmailMessage(email_subject,messages,from_email,tp=[to_email])
    mail.send()

