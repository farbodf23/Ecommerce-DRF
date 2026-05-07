from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .filters import ProductFilter
# Create your views here.


@api_view(["GET"])
def howdy(request: Request):
    if request.method == "GET":
        answer = {"hey": "how you doing"}

        return Response(answer, status=status.HTTP_201_CREATED)


class CategoryList(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None


class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # filter_backends = [SearchFilter, OrderingFilter]
    #
    #    # allowed fields
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['price', 'name', 'created_at']
    filterset_class = ProductFilter

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class ProductDetail(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# @api_view(["GET"])
# def products_of_category(request: Request, name: str):
#     category = get_object_or_404(Category, name__icontains=name)

#     products = Product.objects.filter(
#         category=category, is_active=True
#     ).select_related('category')
#     if not (products.exists()):
#         response = {
#             "detail": "There are not items of this category currently available."}

#         return Response(response, status=status.HTTP_200_OK)

#     serializer = ProductSerializer(
#         products, many=True, context={'request': request})
#     return Response(serializer.data)
