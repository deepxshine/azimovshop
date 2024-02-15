from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .forms import ReviewForm
from .models import Product, Category, User, Favorite, ShoppingCart, Review


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
