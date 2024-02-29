from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg, F

from django.http import Http404

from .forms import ReviewForm
from .models import (Product, Category, User, Favorite, ShoppingCart, Review,
                     Order, ProductsInOrder)


def check(user, product):
    if user.is_authenticated:
        product.in_fav = Favorite.objects.filter(product=product,
                                                 user=user).exists()
        product.in_cart = ShoppingCart.objects.filter(
            product=product, user=user).exists()
    else:
        product.in_fav = False
        product.in_cart = False
    return product


def index(request):
    products: list = Product.objects.all()
    [check(request.user, product) for product in products]
    context = {
        'products': products
    }
    template = 'goods/index.html'
    return render(request, template, context)


def good_info(request, pk):
    product: Product = get_object_or_404(Product, id=pk)
    parameters = product.param.all()
    product = check(request.user, product)
    form = ReviewForm()
    reviews = Review.objects.filter(product=product)
    rating = reviews.aggregate(Avg('rating'))
    context = {
        'product': product,
        'parameters': parameters,
        'form': form,
        'reviews': reviews,
        'rating': rating
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
    [check(request.user, product) for product in products]
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
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk)  # SyntaxError
    user = request.user
    if not ShoppingCart.objects.filter(user=user, product=product).exists():
        ShoppingCart.objects.create(user=user, product=product, count=1)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def del_from_favorite(request, pk):
    product = get_object_or_404(Product, id=pk)
    user = request.user
    favorite = Favorite.objects.filter(user=user, product=product)
    if favorite.exists():
        favorite.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def del_from_shopping_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    user = request.user
    cart = ShoppingCart.objects.filter(user=user, product=product)
    if cart.exists():
        cart.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def favorite_index(request):
    """Созвращать список товаров в избранном"""
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    print(favorites)
    products = [fav.product for fav in favorites]
    [check(user, product) for product in products]
    print(products)
    context = {
        "products": products
    }
    template = 'goods/favorites_list.html'
    return render(request, template, context)


@login_required
def shopping_cart_info(request):
    shopping_cart = ShoppingCart.objects.filter(user=request.user)
    for item in shopping_cart:
        item.sum = item.product.price * item.count
    context = {
        "shopping_cart": shopping_cart
    }
    template = "goods/shopping_cart_info.html"
    return render(request,template,context)


@login_required
def create_review(request, pk):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.product = get_object_or_404(Product, id=pk)
        review.save()
    return redirect('goods:good_info', pk)


@login_required
def shopping_cart_count(request, pk):
    cart = ShoppingCart.objects.get(user=request.user, product__id=pk) # один объект
    print(cart)
    print(request.POST)
    if 'plus.x' in request.POST:
        print("вы нажали плюс")
        cart.count = cart.count+1
        cart.save()
    elif 'minus.x' in request.POST:
        if cart.count == 1:
            cart.delete()
        else:
            cart.count = cart.count - 1
            cart.save()
    return redirect('goods:cart')


@login_required
def create_order(request):
    """
    1) Создает запись в таблице ORDER ✅
    2) В таблицу ProductInOrder добавить товары из корзины
    3) Посчитать сумму одной позиции
    4) Посчитать сумму товаров в таблице ORDER
    5) Удалить корзину
    6) Какое-то сообщение
    """

    cart = ShoppingCart.objects.filter(user=request.user)
    if not cart.exists():
        raise Http404('Not Found')
    order = Order.objects.create(user=request.user, summa=0)
    total_cost = 0

    for cart_product in cart:
        print(cart_product.product.price)
        total_cost += cart_product.product.price * cart_product.count
        print(total_cost)
        ProductsInOrder.objects.create(product=cart_product.product,
                                       count=cart_product.count,
                                       summa=cart_product.product.price,
                                       order=order)
        cart_product.delete()
    order.summa = total_cost
    order.save()
    print(order)
    return redirect("goods:index")


@login_required
def order_history(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    context = {
        "orders": orders
    }
    template = "goods/order_history.html"
    return render(request, template, context)
