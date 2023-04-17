from django.urls import include,path
from . import views

urlpatterns = [
    

       path("checkout/<slug>/", views.checkout_product,name="checkout_product"),
       path("place_order/<slug>/", views.place_order,name="place_order"),
       

   
]

