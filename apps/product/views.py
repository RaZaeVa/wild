from rest_framework import permissions, status, viewsets
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Category, Cart
from .serializers import ProductSerializer, CategorySerializer, ProductCreateSerializer, CartSerializer, \
    CartUpdateSerializer


class ProductListAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ['name']


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [permissions.AllowAny]
