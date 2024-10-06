from user.serializers import UserSerializer
from .models import Cart, CartItem
from rest_framework import serializers
from product.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"

    product = ProductSerializer()


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

    items = CartItemSerializer(many=True)
