from django.shortcuts import render, get_object_or_404

from .models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    template = 'goods/index.html'
    return render(request, template, context)


def good_info(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {
        'product': product
    }
    template = 'goods/good_info.html'
    return render(request, template, context)
