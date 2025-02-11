from django.contrib import admin
from django.urls import path
from .views import login_user, index, products, add_products, edit_products,custom_logout

urlpatterns = [
    path('login/', login_user, name="login"),
    path('', index, name="index"),  
    path('products/', products, name="products"),
    path('add_products/', add_products, name="add_products"),
    path('edit-products/', edit_products, name="edit-products"),
    path('custom_logout/', custom_logout, name="custom_logout"),
    
    
]

