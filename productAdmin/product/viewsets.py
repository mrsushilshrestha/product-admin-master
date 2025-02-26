# from django.contrib.auth.models import User
from .models import Product,Category
from .serializers import ProductSerializer,CategorySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes =[IsAuthenticated]
    # authentication_classes =[JWTAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # pagination_class = MyPageNumberPagination
    queryset =Product.objects.all()
    
    filter_backends=[SearchFilter,DjangoFilterBackend,OrderingFilter]
    Search_fields=['name','description','category__category']
    ordering_fields =['id']
    
    filterset_fields ={
        
        'name': ['exact'],
        'category':['exact'],

    }    
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


