from django.shortcuts import render
from .models import OrderItem


def basket(request):
    items = OrderItem.objects.filter(
        user=request.user,
        status=0
    )
    context = {
        'items': items
    }
    return render(request, 'order/basket.html', context)
