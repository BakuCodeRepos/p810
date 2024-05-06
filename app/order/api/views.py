from rest_framework import generics
from rest_framework.response import Response

from ..models import OrderItem
from .serializers import OrderItemSerializer


class OrderItemCreateAPIView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.user = request.user
        instance.save()
        # increasing count of adding product to basket
        instance.product.adding_to_basket_count += 1
        instance.product.save()

        data = serializer.data

        return Response(data={"detail": "OK", 'data': data}, status=201)
