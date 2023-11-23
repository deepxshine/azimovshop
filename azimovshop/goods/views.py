from django.http import HttpResponse
from django.shortcuts import render

from .models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    template = 'goods/index.html'
    return render(request, template, context)
