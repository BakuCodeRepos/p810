from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, UpdateView
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


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'product'
    template_name = 'product/detail.html'
    slug_url_kwarg = 'slug'