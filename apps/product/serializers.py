from rest_framework import serializers
from .models import Product, Category, Cart
from apps.user.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


