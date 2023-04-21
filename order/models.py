from django.db import models

from products.models import *
from accounts.models import *
# Create your models here.
from accounts.utils import*




class PaymentMethod(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date_order=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField()
    status=models.BooleanField(default=False)
    phone_no=models.CharField(max_length=15,null=True,blank=True)
    adress=models.CharField(max_length=150,null=True,blank=True)
    name=models.CharField(max_length=150,null=True,blank=True)
    city=models.CharField(max_length=150,null=True,blank=True)
    state=models.CharField(max_length=150,null=True,blank=True)
    zipcode=models.CharField(max_length=15,null=True,blank=True)
    payment_Type=models.CharField(max_length=150,null=True,blank=True)
    
    payment_method=models.ForeignKey(PaymentMethod,on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if self.pk is not None:
            orginal = Order.objects.get(pk=self.pk)
            if orginal.status != self.status:
                email_subject = "Congratulation! Your Order is confirmed"
                email_template = "accounts/emails/admin_approve.html"
                context={
                    'user': self.user,
                    'status':self.status
                }
                send_notification(email_subject,email_template,context)
                ...
            else:
                email_subject = "We are sorry! We couldn't accept order."
                email_template = "accounts/emails/admin_approve.html"
                context={
                    'user': self.user,
                    'status':self.status
                }
                send_notification(email_subject,email_template,context)
        return super(Order,self).save(*args, **kwargs)

    


