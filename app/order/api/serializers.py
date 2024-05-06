from rest_framework import serializers
from ..models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = OrderItem
        fields = ['product', 'size', 'color', 'quantity']
