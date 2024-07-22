from django.db.models import Q
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from core.serializers import AllProductSerializer, CategorySerializer
from .models import AllProducts, Category


class AllProductsList(generics.ListAPIView):
    queryset = AllProducts.objects.order_by('-rating')[0:6]
    serializer_class = AllProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    serializer_class = AllProductSerializer

    def get_object(self):
        queryset = AllProducts.objects.all()
        filter_kwargs = {'slug': self.kwargs['product_slug']}
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj


class Search(generics.ListAPIView):
    def get_queryset(self):
        query = self.kwargs.get('query')
        query_upper = query[0].upper() + query[1:]
        query_lower = query[0].lower() + query[1:]
        queryset = AllProducts.objects.filter(Q(name__icontains=query_upper) | Q(name__icontains=query_lower))
        return queryset

    serializer_class = AllProductSerializer


class CreatedFilter(generics.ListAPIView):
    queryset = AllProducts.objects.order_by('-created_at')[0:8]
    serializer_class = AllProductSerializer


class CategoryDetail(generics.ListAPIView):
    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        queryset = AllProducts.objects.filter(category__slug=category_slug)
        return queryset

    serializer_class = AllProductSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

