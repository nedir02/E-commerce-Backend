
from django.urls import path, include

from core.views import *

urlpatterns = [
    path('all-products/', AllProductsList.as_view()),
    path('all-products/<str:product_slug>/', ProductDetail.as_view(), name='product-detail'),
    path('search/<str:query>/', Search.as_view()),
    path('new-products/', CreatedFilter.as_view()),
    path('categories/<str:category_slug>', CategoryDetail.as_view()),
    path('products-by-category/', CategoryListView.as_view(), name='products-by-category'),
]