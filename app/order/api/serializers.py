from rest_framework import serializers
from ..models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = OrderItem
        fields = ['product', 'size', 'color', 'quantity']


class OrderItemDeleteSerializer(serializers.ModelSerializer):    
    class Meta:
        model = OrderItem
        fields = ['id']


class OrderCreateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Order
        fields = ['subtotal', 'total', 'shipping']
