from .models import Category
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST"])
def categories_list(request):
    if request.method == "GET":
        all_categories = CategorySerializer(
            Category.objects.all().order_by("-popularity").values(), many=True
        ).data
        return Response(all_categories)


@api_view(["GET", "PUT", "DELETE"])
def category_details(request, id):
    category = get_object_or_404(Category, id=id)
    return Response(CategorySerializer(category).data)
