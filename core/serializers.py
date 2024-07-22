from rest_framework import serializers

from .models import AllProducts, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name', 'slug']


class AllProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = AllProducts
        fields = (
            'id',
            'name',
            'description',
            'price',
            'main_img',
            'img_1',
            'img_2',
            'img_3',
            'img_4',
            'img_5',
            'created_at',
            'rating',
            'category',
            'slug',
        )