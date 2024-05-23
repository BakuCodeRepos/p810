from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, UpdateView

from order.models import WishList
from .models import Product


# def products(request): # function based product list view
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'product/list.html', context)

class ProductListView(ListView): # class based product list view
    queryset = Product.objects.all()
    context_object_name = 'products' # default name = object_list
    template_name = 'product/list.html'

    def get_queryset(self):
        q = super().get_queryset()
        main_result = []
        for product in q:
            try:
                wish_list = WishList.objects.get(user=self.request.user)
                if product in wish_list.product.all():
                    result = True
                result = False
            except WishList.DoesNotExist:
                result = False
            if result:
                product.added_to_wish_list = True
            else:
                product.added_to_wish_list = False
            product.save()
            main_result.append(product)
        return main_result

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'product'
    template_name = 'product/detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        sizes = [size for size in self.get_object().size]
        context['sizes'] = sizes

        return context
