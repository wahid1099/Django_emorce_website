from django.urls import path,include

from . import views

urlpatterns=[
     path("allproducts/", views.allproducts,name="allproducts"),
     path("search_product/", views.search_view,name="search_product"),

    path("<slug>/", views.get_product,name="get_product"),
    path("review/<uuid:product_id>/", views.review,name="review"),
    path("addReview/<uuid:product_id>/", views.addReview,name="addReview"),
   
    
    
    

]  

