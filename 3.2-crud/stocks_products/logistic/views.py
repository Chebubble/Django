from rest_framework.viewsets import ModelViewSet
<<<<<<< HEAD
=======
from django_filters.rest_framework import DjangoFilterBackend
>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02
from rest_framework.filters import SearchFilter
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
<<<<<<< HEAD
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', ]
=======
    filterset_fields = ['title', 'description']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']


>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02
class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['products']
    search_fields = ['products__title', 'products__description' ]
    
    # при необходимости добавьте параметры фильтрации
<<<<<<< HEAD
    filterset_fields = ['products', ]
=======

>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02
