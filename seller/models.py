from django.db import models
from accounts.models import User,UserProfile
# from accounts.utils import send_notification
# Create your models here.

class Seller(models.Model):
    user=models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)

    user_profile=models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    shop_name=models.CharField(max_length=100,null=True, blank=True)
    shop_license=models.ImageField(upload_to='shop/license',null=True, blank=True)
    is_approved=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.shop_name
    

     