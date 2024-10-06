# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CartSerializer
from .models import Cart
from django.contrib.auth.models import User


@api_view(["GET"])
def fetch_carts(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True).data
    return Response(serializer)


@api_view(["GET", "POST"])
def fetch_cart(request, username):
    user = User.objects.filter(username=username)
    print(user)
    cart = Cart.object.all(user=user)
    print(cart)
    return Response(cart)
