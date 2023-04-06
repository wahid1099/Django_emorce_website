from django import forms

from .models import Seller
class SellerForm(forms.ModelForm):
    class Meta:
        model=Seller
        fields=['shop_name','shop_license']
        