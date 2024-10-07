# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CartSerializer
from .models import Cart, CartItem
from django.contrib.auth.models import User
from product.models import Product


@api_view(["GET"])
def fetch_carts(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True).data
    return Response(serializer)


@api_view(["GET"])
def fetch_cart(request, username):
    user = User.objects.filter(username=username).first()
    print(user)
    cart = Cart.objects.filter(user=user).first()
    print(cart)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(["POST"])
def add_to_cart(request, username):
    print("wahta")
    print(username)
    user = User.objects.filter(username=username).first()
    print(user)
    cart, created = Cart.objects.get_or_create(user=user)
    print(cart)
    product_id = request.data.get("product_id")
    quantity = request.data.get("quantity", 1)
    product = Product.objects.filter(id=product_id).first()
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product, defaults={"quantity": quantity}
    )

    if not created:
        # If the item already exists, update the quantity
        cart_item.quantity += quantity
        cart_item.save()

    # Return the updated cart
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=201)
