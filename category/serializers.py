from rest_framework import serializers
from .models import Category
from product.serializers import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
