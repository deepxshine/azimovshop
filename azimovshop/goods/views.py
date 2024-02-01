from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Category, User, Favorite, ShoppingCart



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
    if request.user.is_authenticated:
        in_fav = Favorite.objects.filter(product=product,
                                        user=request.user).exists()
    else:
        in_fav = False
    context = {
        'product': product,
        'parameters': parameters,
        'in_fav': in_fav,
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


def category_detail(request, slug):
    """
    Должна получить товары в определенной категории
    """
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        "products": products,
        "category": category
    }
    template = 'goods/category_detail.html'
    return render(request, template, context)


def search(request):
    query = request.GET.get('text')
    products = Product.objects.filter(name__icontains=query)
    context = {
        'products': products
    }
    template = 'goods/index.html'
    return render(request, template, context)


@login_required
def profile_detail(request):
    user = get_object_or_404(User, id=request.user.id)

    context = {
        'user': user,
    }
    template = 'goods/profile.html'
    return render(request, template, context)


@login_required
def add_to_favorite(request, pk):
    product = get_object_or_404(Product, id=pk)
    user = request.user
    if not Favorite.objects.filter(user=user, product=product).exists():
        Favorite.objects.create(user=user, product=product)
    return redirect('goods:good_info', pk)


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk)  # SyntaxError
    user = request.user
    if not ShoppingCart.objects.filter(user=user, product=product).exists():
        ShoppingCart.objects.create(user=user, product=product, count=1)
    return redirect('goods:good_info', pk)


@login_required
def del_from_favorite(request, pk):
    product = get_object_or_404(Product, id=pk)
    user = request.user
    favorite = Favorite.objects.filter(user=user, product=product)
    if favorite.exists():
        favorite.delete()
    return redirect('goods:good_info', pk)


@login_required
def del_from_shopping_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    user = request.user
    cart = ShoppingCart.objects.filter(user=user, product=product)
    if cart.exists():
        cart.delete()
    return redirect('goods:good_info', pk)
