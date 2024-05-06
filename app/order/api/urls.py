from django.urls import path

from . import views

urlpatterns = [
    path('order-item-create', views.OrderItemCreateAPIView.as_view(), name='order_item_create'),
]
