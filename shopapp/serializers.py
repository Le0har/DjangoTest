from rest_framework import serializers
from .models import Product, Order
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProductSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Product
        fields = ['pk', 'name', 'description', 'price', 'discount', 'created_at', 'archived', 'author']



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['adress', 'promo', 'created_at', 'user', 'products']