from django.shortcuts import render, get_object_or_404

from .models import Product, Category


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    template = 'goods/index.html'
    return render(request, template, context)


def good_info(request, pk):
    product = get_object_or_404(Product, id=pk)
    parameters = product.param.all()
    context = {
        'product': product,
        'parameters': parameters,
    }

    template = 'goods/good_info.html'
    return render(request, template, context)


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    template = 'goods/category_list.html'
    return render(request, template, context)


def category_detail():
    """
    Должна получить товары в определенной категории
    """
