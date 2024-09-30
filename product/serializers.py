from rest_framework import serializers
from .models import Product
from category.models import Category


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True
    )
    category_name = serializers.StringRelatedField(
        many=True, source="category", read_only=True
    )

    class Meta:
        model = Product
        fields = "__all__"
