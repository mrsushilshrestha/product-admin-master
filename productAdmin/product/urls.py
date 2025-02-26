from django.contrib import admin
from django.urls import path,include
from .views import login_user, index, products, add_products, edit_products,custom_logout,customer_account,customer_setting,delete_product,add_category
from rest_framework import routers
from .viewsets import ProductViewSet,CategoryViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('login/', login_user, name="login"),
    path('', index, name="index"),  
    path('products/', products, name="products"),
    path('add_products/', add_products, name="add_products"),
    path('add_category/', add_category, name="add_category"),
    path('custom_logout/', custom_logout, name="custom_logout"),
    path('customer_account/', customer_account, name="customer_account"),
    path('customer_setting/', customer_setting, name="customer_setting"),
    
    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),
    path('edit-products/', edit_products, name='edit_products'),
    path('api/',include(router.urls))
]

    


