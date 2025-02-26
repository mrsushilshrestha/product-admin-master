# Django REST Framework Guide

## Documentation
- **Django REST Framework:** [Official Documentation](https://www.django-rest-framework.org/)
- **Swagger (drf-yasg):** [PyPI Package](https://pypi.org/project/drf-yasg/)

---

## Setting Up Django REST Framework

### Installation
```sh
pip install djangorestframework
pip install drf-yasg  # For Swagger
pip install django-filter  # For filtering support
```

### Add to `INSTALLED_APPS` in `settings.py`
```python
INSTALLED_APPS = [
    'rest_framework',
    'drf_yasg',  # Swagger Support
    'django_filters',
]
```

### Basic Configuration in `settings.py`
```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

---

## Implementing Filters in Django REST Framework

### Example: Filtering in Django Views

```python
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name', 'description', 'category__category']
    ordering_fields = ['id']
    filterset_fields = {
        'name': ['exact'],
        'category': ['exact'],
    }

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
```

---

## Adding Swagger API Documentation

### Configure Swagger in `urls.py`

```python
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation using Swagger",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your-email@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

### Access API Documentation
- **Swagger UI:** `http://localhost:8000/swagger/`
- **Redoc UI:** `http://localhost:8000/redoc/`

---

## Conclusion
This guide provides a quick setup for Django REST Framework, Swagger API documentation, and filtering in Django. Customize the setup as needed for your project!
