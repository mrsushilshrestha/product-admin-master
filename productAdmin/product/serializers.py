from django.contrib.auth.models import User
from .models import Product,Category
from rest_framework  import serializers

# Serializers define the API representation.
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'description', 'category', 'expire_date','stock','image']
        

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        
