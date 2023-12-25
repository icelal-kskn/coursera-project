from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
        

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'category', 'category_id']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
class CartSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'unit_price', 'price', 'menuitem','menuitem_id','user', 'user_id']
class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    delivery_crew_id = serializers.IntegerField(write_only=True)
    delivery_crew_id = UserSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'status', 'total', 'date', 'user', 'user_id', 'delivery_crew_id', 'delivery_crew']
    
class OrderItemSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = OrderItem
        fields = ['id', 'unit_price', 'price', 'menuitem','menuitem_id','user', 'user_id']