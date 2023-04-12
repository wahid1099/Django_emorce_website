from django.contrib import admin

from .models import Seller
# Register your models here.


class SellerAdmin(admin.ModelAdmin):
    list_display=('user','shop_name','is_approved','created_at')
    list_display_links=('user','shop_name','created_at')
    link_editable=('is_approved')

admin.site.register(Seller,SellerAdmin)