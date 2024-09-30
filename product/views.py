from .models import Product
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST"])
def products_list(request):
    if request.method == "GET":
        search_query = request.GET.get("search", None)
        category_query = request.GET.get("category", None)
        if search_query:
            products = Product.objects.filter(name__istartswith=search_query)
            serializer = ProductSerializer(products, many=True).data
        elif category_query:
            products = Product.objects.filter(category=category_query)
            serializer = ProductSerializer(products, many=True).data
        else:
            serializer = ProductSerializer(Product.objects.all(), many=True).data
        return Response(serializer)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "GET":
        serializer = ProductSerializer(product).data
        return Response(serializer)
    elif request.method == "DELETE":
        product.delete()
        return Response(serializer, status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
