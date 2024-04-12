from rest_framework import serializers
from .models import Category, ProductVariation


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductVariationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductVariation
        fields = ('product_name', 'product_model', 'short_description', 'product', 'features', 'images',
                  'price', 'discount', 'calc_discount', 'quantity', 'is_available', 'created_at')
        depth = 3
